class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    if top is equal to NULL
    newNode -> next= NULL
    else
    newNode -> = top
    
    # Write your code here

  def pop(self) -> None:
    if top==NULL
    print("stack overflow")
    else
    temp=top
    top=temp->next
    free(temp)
    # Write your code here

  def status(self):
    """
    It prints all the elements of stack.
    """
    Traverse till temp=0
    # Write your code here  


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
