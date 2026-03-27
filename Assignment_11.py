# ML Idea Generator
# Example ML problems with input and output
ml_problems = {
"College Performance Prediction": {
"Input": ["Attendance", "Study Hours", "Assignment Marks"],
 "Output": "Predicted Final Grade"
 },
    "Healthcare Disease Prediction": {
 "Input": ["Age", "Symptoms", "Blood Pressure", "Medical History"],
"Output": "Disease Risk Prediction"
},
    "Shopping Product Recommendation": {
 "Input": ["Browsing History", "Purchase History", "User Preferences"],
  "Output": "Recommended Products"
 }}
# Display ML ideas
for problem, details in ml_problems.items():
   print("\nProblem:", problem)
   print("Input Features:", details["Input"])
   print("Output:", details["Output"])
