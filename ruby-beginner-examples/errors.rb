lucky = Array [2,3,1,6]

begin
  lucky["dog"]
  num = 10/0
rescue ZeroDivisionError
  puts "Division by zero error"
rescue TypeError => e
  puts e
end
