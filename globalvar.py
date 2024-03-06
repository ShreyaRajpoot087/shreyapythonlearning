def show_truth():
    global myst_var
    myst_var ='Shreya'
    print(myst_var)

myst_var = 'singh'
print(myst_var)
show_truth()
print(myst_var)
def unique(input_list=[]):
  to_return = []
  for el in input_list:
    if el not in to_return:
      to_return.append(el)
  return to_return

