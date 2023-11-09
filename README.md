# top-down-oop-programming
Top-down oop programming example

NAME

    main

CLASSES

    builtins.object
        BaseObject
            Exam
                GraduationExam
            Test
            TestTrial
        ObjectRegistry
    
    class BaseObject(builtins.object)
     |  BaseObject(name, date)
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name, date)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  info(self)
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  info_date
     |  
     |  info_name
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Exam(BaseObject)
     |  Exam(name, date, subject)
     |  
     |  Method resolution order:
     |      Exam
     |      BaseObject
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name, date, subject)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  info(self)
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  subject_info
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from BaseObject:
     |  
     |  info_date
     |  
     |  info_name
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseObject:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class GraduationExam(Exam)
     |  GraduationExam(name, date, subject, required_score)
     |  
     |  Method resolution order:
     |      GraduationExam
     |      Exam
     |      BaseObject
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name, date, subject, required_score)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  info(self)
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  req_score_info
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from Exam:
     |  
     |  subject_info
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from BaseObject:
     |  
     |  info_date
     |  
     |  info_name
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseObject:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class ObjectRegistry(builtins.object)
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  add_object(self, obj)
     |  
     |  view_list(self)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Test(BaseObject)
     |  Test(name, date, questions)
     |  
     |  Method resolution order:
     |      Test
     |      BaseObject
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name, date, questions)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  info(self)
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  info_questions
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from BaseObject:
     |  
     |  info_date
     |  
     |  info_name
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseObject:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class TestTrial(BaseObject)
     |  TestTrial(name, date, subject, difficulty)
     |  
     |  Method resolution order:
     |      TestTrial
     |      BaseObject
     |      builtins.object
     |  
     |  Methods defined here:
     |  
     |  __init__(self, name, date, subject, difficulty)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  info(self)
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |  
     |  difficulty_info
     |  
     |  subject_info
     |  
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from BaseObject:
     |  
     |  info_date
     |  
     |  info_name
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from BaseObject:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS

    create_exam(registry)
    
    create_graduation_exam(registry)
    
    create_test(registry)
    
    create_test_trial(registry)
    
    int_input(inpt)
    
    main()
    
    test_name_date_input()

FILE
    
    OOP_2/main.py