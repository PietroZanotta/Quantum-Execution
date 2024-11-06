import pickle

# Load the AST from the .ast file
with open("example.ast", "rb") as f:
    ast = pickle.load(f)


