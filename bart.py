from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = """ Solicitation closes:
at – à April 3, 2024
on – le 14:00 (type or print)
1. Headrests (when needed) should include three-way adjustable pivoting ability
2. Backrests must be upholstered with air breathability or mesh option
3. Lumbar support to include independent depth adjustability (such as with a pump)
Page 17 of - de 29
RFPJ074110/A
Table A1: Rotary Chair
CHAIR TYPE: Quantity Required: 2
Y ROTARY CHAIR
N ROTARY STOOL
Instructions to Users:
• Choose the attributes (N→Y) that must be included for your
requirement. Use 1 builder per type of chair.
• Note: if more than 1 “Y” is chosen then all attributes will be
considered acceptable for the requirement.
Y All products meet a minimum of ANSI/BIFMA e3 minimum Level® 2
Y All plastic components are recyclable at the end of their life.
Weight Capacity Y Standard (up to 275 lbs) N Large-occupant (275+ lbs up to 400 lbs)
Usage Y Single shift N 24/7 (3 continuous working shifts, 7 days a week)
A Headrest Y No N Yes (adjustable) N No preference
B Backrest Height Y Standard N High N No preference
N Fixed position Y Adjustable (by user) N Self-Adjusting mechanism N No preference With
C Lumbar Support
lumbar support adjustable with a pump
Y Height Adjustment Armrest Style: cushioned
D Y Adjustable Y Lateral Adjustment Y T-arm (DD) → N Fixed Y Adjustable
Armrests
Y Fully Articulating N Cantilever
N Fixed → N T-arm N Cantilever N Loop N No preference
Y Adjustable 15 inches to 18 inches
E
N Fixed position N Shallow N Medium N Deep
F
Seat Width Y Standard based on weight capacity chosen above (small seat pan)
Rotary Chair N Adjustable – standard range Y Adjustable - low range
G Seat Height
Y Multifunction N Synchro Tilt N Unison Tilt N Weight Sensitive N No
Rotary Chair
preference
H Tilt Mechanism
Y Multifunction N Synchro Tilt N Unison Tilt N Weight Sensitive N Fixed Back
N No preference
Seat Angle and
I Backrest-to-seat Adjustable and lockable (not applicable to weight sensitive tilt mechanisms)
Angle
J Casters for use on: Y carpet Y hard surfaces
L N integrated fixed height N adjustable height
(rotary stools only)
Backrest: Y Upholstery N Non-upholstery (ie. flexible plastic) N Mesh Material
Seat: Y Upholstery N Non-upholstery (ie. flexible plastic) N Mesh Material
Base Frame: N Metal Y Plastic
Y All chairs must be provided with labelling and instructions
Y Not applicable
N Adjustment levers to be equipped with brail
"""
print(summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False))
