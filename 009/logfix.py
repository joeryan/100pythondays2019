# fix remaining dates for the 100days challenge log
from datetime import datetime, timedelta


def extract_entries(logfile):
  with open(logfile, 'r') as infile:
    log_lines = [line.split('|') for line in infile.readlines()]
  new_log_lines = []
  for log_entry in log_lines[1:]:
    entry = [item.strip() for item in log_entry]
    new_log_lines.append(entry)
  return new_log_lines


def adjust_remaining_dates(log_entries):
  new_entries = []
  for entry in log_entries:
    if entry[-2] == 'LEARNING':
      entry[2] = datetime.strftime(datetime.strptime(entry[2], "%b %d, %Y") + timedelta(days=1), "%b %d, %Y")
    new_entries.append(entry)
  return new_entries

def create_new_log(log_entries):
  new_log = []
  for entry in log_entries:
    new_entry = [" {} ".format(item) for item in entry if item ]
    new_entry.append('')
    new_entry.insert(0,'')
    new_log.append('|'.join(new_entry) + '\n')
  return new_log


def main():
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("logfile", help="logfile to correct remaining dates in")
  parser.add_argument("--outfile", help="output file location, relative to working dir", default='LOG.md')
  args = parser.parse_args()
  log_entries = extract_entries(args.logfile) 
  log_entries = adjust_remaining_dates(log_entries)
  new_log =  create_new_log(log_entries) 
  with open(args.outfile, 'w') as outfile:
    outfile.write("## Progress Log\n")
    for line in new_log:
      outfile.write(line)

if __name__ == '__main__':
  main()
