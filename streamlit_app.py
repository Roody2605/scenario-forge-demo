# replace old line ↓
# df = pd.read_csv(uploaded)

# new robust line
df = pd.read_csv(uploaded, engine="python", skipinitialspace=True)
