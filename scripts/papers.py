"""Original department papers plus Version 3 route reviews; three mark points per item."""
P={}
def paper(year,letter,rows):
 P[(year,letter)]=[dict(title=f'Question {i+1}',q=q,m=3,ms=scheme.split('~')) for i,(q,scheme) in enumerate(rows)]
paper(7,'A',[
('A pattern has 6, 10, 14, 18 tiles. State how it changes each time, find the next term and find a rule using the position n.','Add 4~Next term 22~nth term 4n+2'),
('A number machine multiplies an input by 5 and then adds 2. The output is 47. Find the input, showing how you undo the steps.','47−2=45~45÷5~Input 9'),
('Solve 3x+8=35 and check your solution.','3x=27~x=9~3×9+8=35'),
('Order 0.609, 0.69 and 0.069 from smallest to largest. Explain your place-value comparison.','0.069<0.609<0.69~Compare aligned tenths/hundredths/thousandths~0.69=0.690'),
('Calculate 32.4−8.76 and then multiply the result by 0.5. Show both stages.','32.40−8.76=23.64~Half of 23.64~11.82'),
('The travel times are 8, 10, 10, 12 and 15 minutes. Find the median, mean and range.','Median 10 min~Mean 55÷5=11 min~Range 15−8=7 min'),
('Estimate 39.2×5.8 by rounding both values to 1 significant figure. Explain whether an exact answer of 227.36 is sensible.','40×6~Estimate 240~227.36 is reasonably close and sensible'),
('Convert 9/25 to a decimal and percentage, and give an equivalent fraction with denominator 100.','36/100~0.36~36%'),
('At dawn the temperature is −5°C. It rises by 9°C, then falls by 6°C. Find the final temperature.','−5+9=4°C~4−6~−2°C'),
('A jumper costs £48. A sale reduces it by 25%. Find the discount and sale price.','25% of 48=12~48−12~£36')])
paper(7,'B',[
('A rectangular garden is 7.5 m long and 4 m wide. Find its perimeter and area, with units.','Perimeter 2(7.5+4)=23 m~Area 7.5×4~30 m²'),
('A triangle has base 14 cm and perpendicular height 5 cm. State the area formula and calculate its area.','A=½bh~½×14×5~35 cm²'),
('A bus departs at 23:48 and arrives at 00:27 the next day. Find the time taken in minutes and decimal hours.','12+27=39 minutes~39÷60~0.65 hours'),
('A cyclist covers 12 km in 40 minutes. Find average speed in km/h.','40 min=2/3 h~12÷(2/3)~18 km/h'),
('On a distance–time graph, a straight section joins (4 s,6 m) to (10 s,30 m). Find the speed on that section.','Distance change 24 m~Time change 6 s~4 m/s'),
('Write 42 and 70 as products of primes, then find their HCF.','42=2×3×7~70=2×5×7~HCF=14'),
('Two bells ring every 12 and 18 minutes. They ring together at 09:00. When will they next ring together?','Find LCM of 12 and 18~LCM=36 minutes~09:36'),
('Calculate 3/4+5/6 and give a mixed number in simplest form.','9/12+10/12~19/12~1 7/12'),
('An isosceles triangle has a vertex angle of 44°. Find each base angle and explain your reasoning.','Equal base angles~Remaining total 180−44=136°~Each 68°'),
('A pictogram uses one symbol for 6 books. A group has 4½ symbols. Find its number of books and state why the key is essential.','4×6=24~Half symbol 3, total 27~Key links symbols to frequencies')])
paper(8,'A',[
('Share £150 in the ratio 2:3. Show the value of one ratio unit and both shares.','5 units, £30 each~First share £60~Second share £90'),
('A recipe for 4 people uses 300 g of rice. Find the rice for 10 people, using the same amount per person.','300÷4=75 g per person~75×10~750 g'),
('A model uses scale 1:250. A wall is 4.8 cm on the model. Find its real length in metres.','4.8×250=1200 cm~Divide by 100~12 m'),
('Expand and simplify 3(2x−5)+2(x+4).','6x−15+2x+8~Collect like terms~8x−7'),
('Find the equation of a line with gradient 2 through (3,8).','y=2x+c~8=6+c gives c=2~y=2x+2'),
('Calculate 2/3÷5/6 and simplify.','2/3×6/5~12/15~4/5'),
('Reflect (5,−2) in x=1 and explain the distance check.','Point is 4 units right of line~Image 4 units left~(−3,−2)'),
('A cuboid measures 12 cm by 5 cm by 4 cm and has mass 600 g. Find volume and density.','Volume 240 cm³~Density=600/240~2.5 g/cm³'),
('Solve 5x−4<21 and state the largest integer that makes the inequality true.','5x<25~x<5~Largest integer 4'),
('A £160 ticket rises in price by 12.5%. Find the new price using a multiplier.','Multiplier 1.125~160×1.125~£180')])
paper(8,'B',[
('Values 1, 3 and 5 have frequencies 4, 2 and 4. Find the mean.','Products 4,6,20~Total 30 over frequency 10~Mean 3'),
('A regular decagon has 10 sides. Find each exterior angle and each interior angle.','360/10=36° exterior~Interior=180−36~144°'),
('A bag holds 6 red, 3 blue and 3 yellow counters. Find P(red), P(not red), and explain their sum.','P(red)=6/12=1/2~P(not red)=1/2~Complements sum to 1'),
('A club has 18 cyclists and 12 walkers. Of the cyclists, 7 wear a helmet in the survey category. A cyclist is selected. Find P(not in the helmet category).','18−7=11~Sample is 18 cyclists~11/18'),
('A circle has radius 7 cm. Give exact circumference and exact area, including units.','C=2πr=14π cm~A=πr²~49π cm²'),
('A cylinder has radius 3 cm and height 5 cm. A cone has the same dimensions. Find both exact volumes.','Cylinder π×3²×5=45π cm³~Cone one third of cylinder~15π cm³'),
('In a survey of 80 pupils, 30 walk to school. Find the walking sector angle in a pie chart.','Fraction 30/80~Multiply by 360°~135°'),
('A scatter graph shows more revision time going with higher scores. State the correlation and two reasons this does not prove that extra revision caused the higher scores.','Positive correlation~Other factors may affect both~Correlation alone does not prove revision time caused the difference'),
('After a 15% reduction a jacket costs £68. Find its original price.','Remaining multiplier 0.85~68÷0.85~£80'),
('The sides of a triangle are given by x+2, x+3 and x+5 cm. Its perimeter is 31 cm. Find x and the longest side.','3x+10=31~x=7~Longest side 12 cm')])
paper(9,'A',[
('Calculate 4.8÷0.16 and use multiplication to check your answer.','480÷16~30~30×0.16=4.8'),
('Evaluate 16^(−1/2), explaining the root and reciprocal steps.','√16=4~Negative power gives reciprocal~1/4'),
('Given 72=2³×3² and 120=2³×3×5, find their HCF and LCM.','HCF=2³×3=24~LCM=2³×3²×5~360'),
('Calculate (8×10⁵)÷(2×10⁻²) and give the result in standard form.','8÷2=4~Exponent 5−(−2)=7~4×10⁷'),
('Simplify √75 and rationalise 5/√3.','√75=5√3~Multiply numerator and denominator by √3~5√3/3'),
('Expand (2x+3)(x−4) and collect like terms.','2x²−8x+3x−12~Combine x terms~2x²−5x−12'),
('Solve 4(x−2)=2x+10 and check your result.','4x−8=2x+10~x=9~Both original sides equal 28'),
('Make t the subject of v=u+at, stating a restriction on a.','v−u=at~t=(v−u)/a~a≠0'),
('Solve −2<3x+1≤13 and give the integer solutions.','−3<3x≤12~−1<x≤4~Integers 0,1,2,3,4'),
('Find the nth term of 4, 9, 16, 25 and use it to find the eighth term.','Rule n²+2n+1 or (n+1)²~Substitute n=8~81')])
paper(9,'B',[
('Convert 0.454545… to a simplified fraction using algebra.','100x−x=45~99x=45~5/11'),
('£400 grows by 5% each year for two years. Find the final value and explain why adding 10% gives a different result.','400×1.05²~£441~Second year uses the increased balance, so £440 from simple addition differs'),
('Red:blue=2:3 and blue:green=6:5. Find a single ratio red:blue:green.','Match blue at 6~Red:blue=4:6~4:6:5'),
('A right triangle has hypotenuse 17 cm and one shorter side 8 cm. Find the other side.','Other side²=17²−8²~225~15 cm'),
('A ladder has length 10 m and makes angle 30° with the ground. Find its vertical height and state the right-triangle ratio.','sin30°=height/10~Height=10×0.5~5 m'),
('A grouped class 20≤x<35 has frequency 24. Find its histogram frequency density and explain why class width matters.','Width 15~Density 24/15=1.6~Frequency is proportional to bar area'),
('Explain interpolation and extrapolation on a scatter graph and state which normally has more support from the measured data.','Interpolation predicts within observed range~Extrapolation predicts outside it~Interpolation normally has stronger support, since trend continuation outside is uncertain'),
('Velocity rises uniformly from 0 to 12 m/s in 5 s. Find acceleration and distance travelled.','Acceleration 12/5=2.4 m/s²~Distance is triangular area~½×5×12=30 m'),
('Find the equation of the line through (−1,1) and (3,9).','Gradient (9−1)/(3−(−1))=2~1=2(−1)+c gives c=3~y=2x+3'),
('For y=x²−16, find both x-intercepts and the y-intercept.','At y=0, x²=16~x=−4 and 4~At x=0, y=−16')])
