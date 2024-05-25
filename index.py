from collections import defaultdict

class LogEntry:
    def __init__(self, timestamp, log_type, severity):
        self.timestamp = timestamp
        self.log_type = log_type
        self.severity = severity

class LogMonitor:
    def __init__(self):
        self.log_entries = []
        self.log_types = defaultdict(list)

    def submit_log_entry(self, timestamp, log_type, severity):
        entry = LogEntry(timestamp, log_type, severity)
        self.log_entries.append(entry)
        self.log_types[log_type].append(entry)

    def get_severity_stats(self, log_entries):
        if not log_entries:
            return 0.0, 0.0, 0.0

        severities = [entry.severity for entry in log_entries]
        min_severity = min(severities)
        max_severity = max(severities)
        mean_severity = sum(severities) / len(severities)

        return min_severity, max_severity, mean_severity

    def process_command(self, command):
        command_parts = command.split(' ', 1)
        operation = int(command_parts[0])
        output = ""
        filtered_entries = []  # Initialize filtered_entries with an empty list

        if operation == 1:
            try:
                timestamp, log_type, severity = command_parts[1].split(';')
                timestamp = int(timestamp)
                severity = float(severity)
                self.submit_log_entry(timestamp, log_type, severity)
                output = "No output"
            except ValueError:
                output = "Error: Invalid command format. Expected 3 values separated by semicolons."

        elif operation == 2:
            log_type = command_parts[1]
            min_severity, max_severity, mean_severity = self.get_severity_stats(self.log_types[log_type])
            output = f"Min: {min_severity:.2f}, Max: {max_severity:.2f}, Mean: {mean_severity:.6f}"

        elif operation == 3:
            try:
                timestamp_filter, timestamp = command_parts[1].split()
                timestamp = int(timestamp)
                if timestamp_filter == "BEFORE":
                    filtered_entries = [entry for entry in self.log_entries if entry.timestamp < timestamp]
                else:
                    filtered_entries = [entry for entry in self.log_entries if entry.timestamp > timestamp]
                min_severity, max_severity, mean_severity = self.get_severity_stats(filtered_entries)
                output = f"Min: {min_severity:.2f}, Max: {max_severity:.2f}, Mean: {mean_severity:.6f}"
            except ValueError:
                output = "Error: Invalid command format. Expected timestamp and filter."

        elif operation == 4:
            try:
                timestamp_filter, log_type, timestamp = command_parts[1].split()
                timestamp = int(timestamp)
                if timestamp_filter == "BEFORE":
                    filtered_entries = [entry for entry in self.log_types[log_type] if entry.timestamp < timestamp]
                elif timestamp_filter == "AFTER":
                    filtered_entries = [entry for entry in self.log_types[log_type] if entry.timestamp > timestamp]
                else:
                    output = "Error: Invalid timestamp filter. Must be 'BEFORE' or 'AFTER'."
                    return output  # Return here to avoid executing the code below if the filter is invalid
                #if not filtered_entries:
                #    output = "No logs found for the given filter."
                #    return output  # Return here to avoid processing severity stats on an empty list
                min_severity, max_severity, mean_severity = self.get_severity_stats(filtered_entries)
                output = f"Min: {min_severity:.2f}, Max: {max_severity:.2f}, Mean: {mean_severity:.6f}"
            except ValueError:
                output = "Error: Invalid command format. Expected log type, timestamp filter, and timestamp."


        return output

def main():
    log_monitor = LogMonitor()
    output_lines = []

    try:
        with open('input.txt', 'r') as file:
            commands = file.readlines()

        for command in commands:
            output = log_monitor.process_command(command.strip())
            if output:
                output_lines.append(output)
    except FileNotFoundError:
        print("Error: input.txt not found.")

    # Write output to output.txt
    try:
        with open('output.txt', 'w') as file:
            for line in output_lines:
                file.write(line + '\n')
        print("Output written to output.txt")
    except Exception as e:
        print(f"An error occurred while writing to output.txt: {e}")

if __name__ == "__main__":
    main()
