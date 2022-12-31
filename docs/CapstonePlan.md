# Capstone Plan

## :dizzy: Topic
Human De-Identification Solution upon Videos  
  

## :round_pushpin: Research Steps:
1. Frame Separation:  
Decompse video to frame images
2. Face Detection:  
Detect faces and each of positions
3. Face Landmark Recognition:  
Find facial landmarks from each faces from _step2_
4. De-Identification1 - `Face Swap`:  
Swap face components(eyes, nose, mouth) to unidentified facial component
5. De-Identification2 - Advancement(`Singular value decomposition`):  
Process SVD calculation to make image better
6. De-Identification3 - Handling People:  
Implement solution to handle people(not person)
7. Compose as Video(From frames):  
Combine frames and create output as video