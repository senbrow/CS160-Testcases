# CS160 Winter 2012 Testcases for the SIMPLE language.

* Files starting with valid.\* should parse with *no* errors.

* Files starting with invalid.\* should *not* parse and should throw an error.

* You should be able to run a testcase with `./simple testcases/<a file from
  the repository>` with one of the two configurations below.

## Usage

> NOTICE: Git is preinstalled on CSIL machines.

### On copying the code to your machine

#### As a git Submodule (if you're doing the project with Git) 

You can add this repository as a submodule to the git
repository for your project by doing this:

1. `cd your_cs160_project`

2. `git submodule add "https://github.com/senbrow/CS160-Testcases.git" testcases`

When you need to update the test cases, cd to the `testcases` folder and do `git
pull`.

#### As a seperate folder (if your project is not under version control)

You really should be using version control for your projects. The great thing
about git is that you can start version control with a plain `git init`.
Anyway, maybe next quarter. For now though: 

1. `cd your_cs160_project`

2. `git clone "https://github.com/senbrow/CS160-Testcases.git" testcases`

When you need to update the test cases, cd to the `testcases` folder and do `git
pull`.

### On running your program against testcases en masse

> WHEN COPYING TO YOUR MAKEFILE, make sure you use TABS and not spaces for
> indenting.

Assuming you used one of the schemes above, copy this into your `Makefile` 
and run:

* `make valid_testcases` will test your SIMPLE program against the valid
  testcases 
* `make invalid_testcases` will test your SIMPLE program against the invalid
  testcases
* `make testing` will test your SIMPLE program against all the testcases

```
INVALID_TESTS := ${shell find . -name "invalid.*"}
VALID_TESTS := ${shell find . -name "valid.*"}

valid_testing: $(VALID_TESTS) $(TARGET)
	@echo "STARTING $@"
	@$(foreach var, $(VALID_TESTS), echo "testing $(var)";./simple < $(var);)
	@echo "ENDING $@"

invalid_testing: $(INVALID_TESTS) $(TARGET)
	@echo "STARTING $@"
	@$(foreach var, $(INVALID_TESTS), echo "testing $(var)";./simple < $(var);)
	@echo "ENDING $@"

testing: valid_testing invalid_testing
```

## How to contribute

Fork senbrow's CS160-Testcases repositoty in Github. `cd` to the `testcases` folder,
and do:
    
1. `git remote add <insert your user name here> git://github.com/<insert your user name here>/test.git`

2. `git add <the file you want to add>`

3. `git push <your user name here> master`

Then go on Github and do a pull request (the button is on your fork of the
repository asking Sean to pull from your repository's master branch.

**If you can't figure this out just email us the test case or make an issue with
the code in it.**

