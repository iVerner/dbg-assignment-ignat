# `MORSE CODE Encoder/Decoder`

## Task Description
In this assignment you have to implement a REST Webservice in Python which will convert simple english text to morse code (encode) and morse code to simple english text (decode).

### Morse Code Encoding/Decoding Rule
* Please follow only the alphabet and number encoding from the following link:
https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg

* Use `one space` to indicate the gap between two letters within a word

* Use `two spaces` to indicate the gap between two words

* `Extended` morse code rule:

```
'.' = '.-.-.-'
',' = '--..--'
'?' = '..--..'
```

### `undefined` Rule
* If the english text contains any other charecters except `alphabet`, `number` or the `extended`, please print `/` to indicate `undefined`.

* Again, If the morse code contains any code which is not presented in the rule then print `/` in the translated english text to indicate `undefined`.

### API End Points
In order to accomplish the goal your REST webservice should expose two api end points:

1. `POST /encode`: this end point accepts a text file containing message in English as input and return equivalent morse code of the message as JSON response.

    **Sample Request**: (Assuming the web service is running in localhost at port 5000)

    `curl -X POST -F file=@path_to_file/SampleEnglish.txt http://localhost:5000/encode`
    
    **Sample Response**: (Assuming the SampleEnglish.txt file contains the text `This is a simple text`)
    
    ```
      HTTP/1.1 200 OK
	    Content-Type: application/json
	    Content-Length: **

	    { "result": "- .... .. ...  .. ...  .-  ... .- -- .--. .-.. .  - . -..- -" }
    ```
    
2. `POST /decode`: this end point accepts a text file containing morse code as input and return translated English message as JSON response.

    **Sample Request**:

    `curl -X POST -F file=@path_to_file/SampleMorse.txt http://localhost:5000/decode`
    
    **Sample Response**: (Assuming the SampleMorse.txt file contains the morse code to be decoded)
    
    ```
      HTTP/1.1 200 OK
	    Content-Type: application/json
	    Content-Length: **

	    { "result": "This is a simple text" }
    ```
    
 ## Requirements
 - Python2 / Python3 as programming language
 - Maintainablity - your code should be maintainable; ee value how you structure, write, document code
 - Testability - Please add some tests to showcase your code testability
 - Scalability - please consider, what will happen if N (i.e. N=1000) number of con-current requests come to the API end points
 and how to handle the load
 - (Optional) Deployable - how would you orchestrate the code, so that the web service could be deploy to different environments,
 such as - local (dev), test, stage, production.
 
 
 ## Submission Requirements:
 - Please submit your solution into this private repository in a separate branch.
 - Please give clear instruction about how to run and test the code. You may add the instructions in this README file.
 - We encourage you to use 4 hours for this assignment.

## Usage instructions:
 - You have installed flask dependency in an python environment where you want to run service:
 ```
 pip install flask
```
 - You can run service from the containing module directory with command:
  ```
 python3 -m dbg_assignment_ignat
```