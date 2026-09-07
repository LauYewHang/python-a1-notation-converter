# Test note
To compile and run the unit test, do:
- Get to the directory that consist this folder.  
  I.e.
    ```
    project/ 
        |---- py-int-to-a1/
        |       |---- src/a1_notation_converter/
        |       |---- tests/
        |       |---- .gitignore
        |       |---- LICENSE
        |       |---- pyproject.toml
        |       |---- README.md
        |---- folderA/
        |---- folderB/
        |---- folderC/
    ```
You should be at the `project` directory.

- Run the command:  
`py -m py-int-to-a1.tests.test_int_to_a1`  
`py -m py-int-to-a1.tests.test_a1_to_int`  
To run the respective unit test.