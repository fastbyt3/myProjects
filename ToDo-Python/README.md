# TODO - CLI app in Python

### Functionalities

1. Add new tasks to do
2. Update status of existing status
	- ToDo
	- Curr
	- Done
3. Delete existing tasks


### Implementation

##### .todo file

- stored at `/home/<username>/.todo` or `C:\\User\\<username>\\.todo`

```
1. [STATUS] [DATE TIME] [TASK]
2. [STATUS] [DATE TIME] [TASK]
3. [STATUS] [DATE TIME] [TASK]
...
...
```

##### Order on how I'm gonna do it

1. Figure out how to store the tasks in `.todo` file
2. Code the flags used in Argument parsing - Using _argparse_
3. Add a splash of colors