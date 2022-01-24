class student
  attr_ancestor :name, :major, :gpa
  def initialize (name, major,gpa)
    @name = name
    @major = major
    @gpa = gpa
  end

  def has_honors
    if @gpa >= 3.5
      return true
    end
    return false
  end
end

student1 = student.new("Jim", "Business", 2.6)
student2 = student.new("Mia", "Model", 1.0)
