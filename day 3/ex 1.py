import numpy as np
marks = np.array([45, 67, 89, 34, 78, 90, 56, 49, 72, 61])
print("Marks:", marks)
print("Mean:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Standard Deviation:", marks.std())
passed = marks >= 50
print("Students Passed:", passed.sum())
print("\nSummary Report")
print("Total Students:", len(marks))
print("Passed:", passed.sum())
print("Failed:", len(marks) - passed.sum())
