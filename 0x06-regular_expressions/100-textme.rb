#!/usr/bin/env ruby

# Extract [SENDER], [RECEIVER], and [FLAGS] using regex
matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)

if matches.any?
  # Extract values from the first match
  sender = matches[0][0]
  receiver = matches[0][1]
  flags = matches[0][2]

  # Add a column before joining the values
  result = "#{sender},#{receiver},#{flags}"

  # Print the result
  puts result

end
