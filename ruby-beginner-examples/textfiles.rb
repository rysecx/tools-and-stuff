File.open("employees.txt", "r") do |file| # places the file items in the variable file
  # puts file.readline()  | Puts first line
  # puts file.readlines() | Puts all lines
  # puts file.read()      | Puts all lines
  for line in file.readlines()
    puts line
  end
end

File open("employees.txt", "r") do |file|
  file.write("\nOscar, Accounting")
end

File open("employees2", "w") do |file|
  file.write("Later Bitches")
end

File open("index.html", "w") do |file|
  file.write("<h1>Header1</h1>")
end

# file.readchar()
