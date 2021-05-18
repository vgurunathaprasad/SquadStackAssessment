# SquadStack Assessment
### Parking Lot Management System

The 'assessment.py' is a very simple and straight functional implementation created to see how the parking system flow described in the document works.

### After puting on the Back End Developer Cap
----------------------------------------------

Just like any other sub system, the parking lot management also needs a Repository( to deal with store and retrival), Service (to deal with the business logic) and a controller (for interfacing)

So, Here are the Respcective files and I think the code speaks for itself(I am keeping my fingers crossed, that you will feel the same).
One more thing, the controller work is done in the main.py, hence I thought implementing ParkingSlotController.py is unnecessary.


### More work
--------------

Just like any other piece of code, this project can also be improved.

1. First thing that comes to my mind is, parsing the input. I think if the input is parsed with a regular parser like ANTLR, things will get much simple.
* Mistakes in input can be easily gathered
* The visitor pattern would make implementation much easier
* Will get a DSL(Domain Specific Language) feel... Just for parking lot management

### How to run
--------------

* Clone the repo with:
```
git clone https://github.com/vgurunathaprasad/SquadStackAssessment.git
```

* Open Terminal or Command Prompt, switch to cloned directory ```cd SquadStackAssessment```
* Make sure you have ```Python 3.x``` with ```python -v```
* Run ```main.py``` as ```python main.py``` or ````python3 main.py```
* You will see a prompt with ```#``` ready to get input
* Use [query sample](https://gist.github.com/agrawal-vatsal/19d2c4fb7b7aacda8fb4672aad68e0c9) as reference to interact with the shell
* Type ```Quit``` to exit the shell

