from classArray import Array
DEFAULT_CAPACITY = 5
logicalSize = 5
a = Array(DEFAULT_CAPACITY)
print("Default size  ",len(a))
if logicalSize == len(a):
  temp = Array(len(a) + 1)# Create a new array
for i in range(logicalSize): # Copy data from the old
  temp [i] = a[i] # array to the new array
  a = temp


DEFAULT_DCAPACITY = 20
logicalDSize = 4
a = Array(DEFAULT_DCAPACITY)
print("Default size  ",len(a))
if logicalDSize <= len(a) // 4 and len(a) >= DEFAULT_DCAPACITY * 2:
    temp = Array(len(a) // 2) # Create new array
for i in range(logicalDSize): # Copy data from old array
  temp [i] = a [i] # to new array
  a = temp # Reset old array variable to

# Increase physical size of array if necessary
# Shift items down by one position
for i in range(logicalSize, targetIndex, -1):
  a[i] = a[i - 1]
# Add new item and increment logical size
  a[targetIndex] = newItem
  logicalSize += 1


# Shift items up by one position
for i in range(targetIndex, logicalSize - 1):
  a[i] = a[i + 1]
# Decrement logical size
  logicalSize -= 1
# Decrease size of array if necessary
