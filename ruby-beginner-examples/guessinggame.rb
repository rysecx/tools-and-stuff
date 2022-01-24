secret_word = "Loser"
guess = ""
access = false
attemps = 0

while access == false
  if guess == secret_word
    puts "Well done!"
    puts ("You needed "+ attemps.to_s + " attemps to solve.")
    access = true
  else
    print "Have a try: "
    guess = gets.chomp()
    attemps += 1
  end
end
