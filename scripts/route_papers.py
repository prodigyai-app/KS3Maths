"""Original review questions sampling each year's Version 3 route; not official papers."""
from papers import paper

paper(7,'C',[
 ('A tile pattern has 4, 7, 10, 13 tiles. Give the next two terms and explain why the sequence is linear.','The next term is 16.~The following term is 19.~The difference stays 3 each time.'),
 ('A function machine multiplies by 4, then subtracts 1. Its output is 31. Find the input and check it.','Undo the subtraction: 31 + 1 = 32.~Undo the multiplication: 32 ÷ 4 = 8.~Check: 8 × 4 − 1 = 31.'),
 ('Four numbers have a mean of 7. Three numbers are 3, 6 and 9. Find the missing number.','The required total is 4 × 7 = 28.~The known total is 3 + 6 + 9 = 18.~The missing number is 28 − 18 = 10.'),
 ('A composite bar shows 7 walkers and 5 cyclists on Monday. What total does the bar show? Explain how to draw dual bars for the same data.','The total is 7 + 5 = 12 pupils.~Dual bars would show separate heights of 7 and 5 for Monday.~Use a common scale and a key identifying walkers and cyclists.'),
 ('Write 2/5 as a decimal and percentage. Explain using an equivalent fraction with denominator 100.','2/5 = 40/100.~The decimal is 0.4.~The percentage is 40%.'),
 ('Calculate 3 − (−5). Explain using positive and negative counters or a number line.','Subtracting −5 has the effect of adding 5.~A number line moves five steps right from 3; or add five zero pairs and remove five negative counters.~The answer is 8.'),
 ('Three eighths of a number is 27. Draw or describe an equal-part bar and find the whole.','Three of eight equal parts represent 27.~One part is 27 ÷ 3 = 9.~The whole is 8 × 9 = 72.'),
 ('A 9 cm by 7 cm rectangle has a 3 cm by 2 cm corner removed. Find the remaining area, with units.','The full rectangle has area 9 × 7 = 63 cm².~The removed corner has area 3 × 2 = 6 cm².~The remaining area is 57 cm².'),
 ('A cyclist travels 6 km in 30 minutes. Convert the time to hours, then find the average speed in km/h.','30 minutes = 0.5 hours.~Speed = distance ÷ time = 6 ÷ 0.5.~Average speed = 12 km/h.'),
 ('An isosceles triangle has a top angle of 44°. Find each of its two equal base angles, explaining the rules used.','Triangle angles total 180°, so the two base angles total 136°.~The base angles are equal in an isosceles triangle.~Each is 136 ÷ 2 = 68°.')])

paper(8,'C',[
 ('Red:blue = 2:5. There are 21 more blue counters than red. Find both amounts.','The difference is 5 − 2 = 3 equal parts, so one part is 7.~Red = 2 × 7 = 14.~Blue = 5 × 7 = 35.'),
 ('At the stated rate £1 = €1.25, convert €75 to pounds. Explain how a conversion graph would show this constant rate.','75 ÷ 1.25 = £60.~A graph uses labelled pound and euro axes with even scales.~It is a straight line through the origin, including the point (£60, €75).'),
 ('Factorise 10x + 15 fully. Check by expanding and describe an equal-row tile arrangement.','10x + 15 = 5(2x + 3).~Expanding gives 5 × 2x + 5 × 3 = 10x + 15.~Five equal rows each contain two x-tiles and three unit tiles.'),
 ('A jacket costs £68 after a 15% reduction. Find the original price and check your result.','£68 is 85% of the original, giving multiplier 0.85.~68 ÷ 0.85 = £80.~Check: 80 × 0.85 = £68.'),
 ('A linear sequence is 4, 9, 14, 19, … Find its nth-term rule and its twentieth term.','The common difference is 5, so start with 5n.~The rule is 5n − 1.~The twentieth term is 5 × 20 − 1 = 99.'),
 ('A solid has mass 240 g and volume 80 cm³. State the density formula and calculate its density with units.','Density = mass ÷ volume.~240 ÷ 80 = 3.~The density is 3 g/cm³.'),
 ('Simplify a³ × a⁵ ÷ a² and state any restriction on a.','Multiplication gives a⁸.~Division gives a⁶.~a must not be zero because a² is a divisor.'),
 ('Of 40 pupils, 24 walk. Of the walkers, 16 carry a bag. Find the number who do not walk and the probability that a randomly selected walker carries a bag.','40 − 24 = 16 pupils do not walk.~The selected group has 24 walkers, not 40 pupils.~The probability is 16/24 = 2/3.'),
 ('A semicircle has radius 6 cm. Find its exact area and full perimeter.','Area = ½ × π × 6² = 18π cm².~Curved edge = ½ × 2π × 6 = 6π cm.~Full perimeter = 6π + 12 cm, including the diameter.'),
 ('Times are grouped into 0 ≤ t < 10 with frequency 4 and 10 ≤ t < 20 with frequency 6. Estimate the mean time and explain why it is an estimate.','Use midpoints 5 and 15: the weighted total is 4 × 5 + 6 × 15 = 110.~Divide by 10 values: estimated mean = 11.~Exact values inside the classes are unknown.')])

paper(9,'C',[
 ('Use prime factors to find the HCF and LCM of 18 and 30.','18 = 2 × 3² and 30 = 2 × 3 × 5.~Shared factors give HCF = 2 × 3 = 6.~All required prime powers give LCM = 2 × 3² × 5 = 90.'),
 ('£1000 earns 5% compound interest per year for two years. Find the final balance and explain why it is not £1100.','Use multiplier 1.05 twice: 1000 × 1.05².~The final balance is £1102.50.~The second year earns interest on the first year’s interest as well as on the original £1000.'),
 ('A closed cuboid is 2 cm by 3 cm by 7 cm. Find its surface area.','The three face-pair areas are 6, 14 and 21 cm².~Each occurs twice: 2(6 + 14 + 21).~The surface area is 82 cm².'),
 ('Solve 3x + 7 = 5x − 9 and check the result.','Subtract 3x and add 9 to get 16 = 2x.~x = 8.~Both sides equal 31 when x = 8.'),
 ('A tank starts with 20 litres. Water flows in at 9 litres/min and out at 4 litres/min. Find the volume after 6 minutes.','Net rate is 9 − 4 = 5 litres/min.~The increase is 5 × 6 = 30 litres.~The final volume is 20 + 30 = 50 litres.'),
 ('An example £600 loan has 12 repayments of £56 and a separate £10 fee. Find the total repaid and the extra cost over the amount borrowed.','Repayments total 12 × 56 = £672.~Including the fee, the total repaid is £682.~The extra cost is 682 − 600 = £82.'),
 ('Describe a ruler-and-compasses construction of the perpendicular bisector of a 10 cm segment. Explain why the compass radius must exceed 5 cm.','Draw equal-radius arcs above and below from both endpoints.~Join the two arc intersections; this line bisects the segment at 90°.~A radius greater than half the segment allows two distinct intersections.'),
 ('A Venn diagram has A only 4, both 3, B only 5 and neither 8. Find P(A ∪ B) and P(A ∩ B).','There are 4 + 3 + 5 + 8 = 20 outcomes.~The union contains 12, so P(A ∪ B) = 12/20 = 3/5.~The intersection contains 3, so P(A ∩ B) = 3/20.'),
 ('Find the y-intercept of y = 2ˣ. Explain why y = 1/x has no y-intercept.','At x = 0, 2⁰ = 1, so the exponential graph crosses at (0,1).~A y-intercept requires x = 0.~1/0 is undefined, so the reciprocal graph has no point there.'),
 ('Enlarge point (3,2) by scale factor 2 from centre (1,1). Find the image and explain the movement from the centre.','The original offset from the centre is (2,1).~Doubling the offset gives (4,2).~Add the centre back: the image is (5,3).')])

COVERAGE={
 7:['Sequences','Functions','Averages','Graphing data','Fractions, decimals and percentages','Directed number','Fractions of amounts','Area','Speed','Angles'],
 8:['Ratio','Conversions','Factorising','Percentages','Sequences','Density','Indices','Frequency trees','Circles','Grouped data'],
 9:['Number properties','Compound interest','Surface area','Equations','Rates','Maths and money','Constructions','Sets and probability','Non-linear graphs','Transformations'],
}
