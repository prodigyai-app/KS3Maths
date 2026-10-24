"""Calculation-first examples. Each row is working | optional short annotation.

Keep these separate from assessment wording: changing an example must never
change a saved answer, marking scheme or assignment.
"""
DATA = r"""
sequence: 5, 9, 13, 17 | +4 each time ~ 17 + 4 = 21 ~ 21 + 4 = 25
nonlinear: 1, 4, 9, 16 | Square numbers ~ +3, +5, +7 | Gaps grow by 2 ~ 3 → 6 → 12 → 24 | A different pattern: ×2
nth: 7, 11, 15, 19 | Gap = 4 ~ 4n + 3 | Add 3 to multiples of 4 ~ 4 × 20 + 3 = 83 | Term 20
function: 6 → ×3 → 18 → +4 → 22 | Forward ~ 31 − 4 = 27 | Work backwards ~ 27 ÷ 3 = 9 | Input = 9
notation: a = 4 ~ 3a² = 3 × 16 = 48 | Square a first ~ (3a)² = 12² = 144 | Square everything in brackets
substitute: x = −3, y = 2 ~ x² − 4y = (−3)² − 4 × 2 | Put the values in ~ = 9 − 8 ~ = 1
balance: x + 8 = 19 ~ x = 19 − 8 | Subtract 8 from both sides ~ x = 11 ~ 11 + 8 = 19 ✓ | Check
like: 5a + 3b − 2a + b ~ = (5a − 2a) + (3b + b) | Group like terms ~ = 3a + 4b
equation: 3x + 5 = 26 ~ 3x = 21 | Subtract 5 from both sides ~ x = 7 | Divide both sides by 3 ~ 3 × 7 + 5 = 26 ✓ | Check
place: 0.47 = 0.470 | Add a zero to compare ~ 0.407 < 0.470 | Compare the hundredths
round-dp: 2.30 —— 2.35 —— 2.37 —— 2.40 | Midpoint = 2.35 ~ 2.37 ≈ 2.4 | Nearest tenth
round: 0.006847 → 0.0068 | 2 significant figures ~ 6, 8 → next digit 4 | Keep the 8
standard: (3 × 10⁵) × (4 × 10³) ~ = 12 × 10⁸ | Multiply numbers; add powers ~ = 1.2 × 10⁹ | First number must be below 10
add: 13.70 − 8.46 ~ = 5.24 | Line up decimal points ~ 8.46 + 5.24 = 13.70 ✓ | Check
multiply: 24 × 35 = 840 ~ 2.4 × 0.35 = 0.840 | 3 decimal places in total ~ = 0.84
divide: 6.3 ÷ 0.3 ~ = 63 ÷ 3 | Multiply both numbers by 10 ~ = 21 ~ 21 × 0.3 = 6.3 ✓ | Check
order: 18 ÷ 3 × 2 ~ = 6 × 2 | Work left to right ~ = 12
mean: 2, 3, 3, 8 ~ Mean = 16 ÷ 4 = 4 | Total ÷ number of values ~ Median = 3; mode = 3 | Middle; most common ~ Range = 8 − 2 = 6 | Largest − smallest
missing-average: 4 values; mean = 6; known: 3, 5, 7 ~ Total = 4 × 6 = 24 ~ Known total = 3 + 5 + 7 = 15 ~ Missing value = 24 − 15 = 9
frequency: Value: 1, 2, 3; frequency: 2, 5, 3 ~ Total = 1 × 2 + 2 × 5 + 3 × 3 = 21 ~ Count = 2 + 5 + 3 = 10 ~ Mean = 21 ÷ 10 = 2.1
estimate: 19.6 × 4.8 ≈ 20 × 5 = 100 | Estimate ~ 11.5 cm ≤ length < 12.5 cm | Rounds to 12 cm
charts: ● = 4 pupils | Key ~ ● ● ◐ | 2½ symbols ~ 4 + 4 + 2 = 10 pupils
bar-charts: Year 7: 6; Year 8: 4 | Monday's club ~ 6 and 4 | Two separate bars ~ 6 + 4 = 10 | One stacked bar
first-quadrant: (0,0) → (3,0) | 3 right ~ (3,0) → (3,2) | 2 up ~ (3,2) | Mark the point
scatter: Hot weather → more ice creams ~ Hot weather → more sunburn ~ Ice creams ≠ cause of sunburn | A shared cause affects both
time-series: Day: 0 → 2 → 4 ~ Height: 4 → 7 → 10 cm | +3 cm every 2 days ~ (0,4), (2,7), (4,10) | Plot these points
graph-relationships: x: 0, 1, 2 ~ y = 2x: 0, 2, 4 | Equal increases: +2 ~ y = x²: 0, 1, 4 | Unequal increases: +1, +3
coordinates: A(−2,3), B(6,7) ~ x = (−2 + 6) ÷ 2 = 2 | Average the x values ~ y = (3 + 7) ÷ 2 = 5 | Average the y values ~ Midpoint = (2,5)
fdp: 3/8 = 3 ÷ 8 = 0.375 ~ 0.375 × 100 = 37.5 ~ 3/8 = 37.5% ~ 1.25 = 125% | More than one whole
equivalent: 2⅓ = (2 × 3 + 1)/3 = 7/3 ~ 3/4 = 6/8 > 5/8 | Same denominator ~ 18/24 = 3/4 | Divide top and bottom by 6
fraction-order: 0 → ¼ → ½ → ¾ → 1 → 1¼ | Equal quarter steps ~ ¾ < 1 < 1¼
directed: −4 + 7 = 3 | Move 7 right ~ 5 − (−3) = 5 + 3 = 8 ~ 2 − (−6) = 8°C | Rise from −6°C to 2°C
zero-pairs: (+) (+) | Start at +2 ~ (+) (+) (+) (−) | Add a zero pair ~ (+) (+) (+) | Remove one negative ~ 2 − (−1) = 3
negative-products: (−6) × (−4) = 24 | Two negatives give a positive ~ 24 ÷ (−4) = −6 ~ (−3)² = 9; −3² = −9 | Brackets change what is squared
indices: 8⁽²ᐟ³⁾ | Cube root, then square ~ ∛8 = 2 ~ 2² = 4
fraction-amount: 3/5 of 80 ~ 80 ÷ 5 = 16 | One fifth ~ 16 × 3 = 48 | Three fifths
fraction-whole: 3/5 of the whole = 42 ~ 42 ÷ 3 = 14 | One fifth ~ 14 × 5 = 70 | Five fifths
percent-amount: 15% of £80 ~ 10% = £8 | Divide by 10 ~ 5% = £4 | Half of 10% ~ 15% = £8 + £4 = £12
change: £50 → £65 ~ Change = 65 − 50 = £15 ~ 15 ÷ 50 × 100 = 30% | Divide by the original
reverse: 80% = £64 | After a 20% reduction ~ 100% = 64 ÷ 0.8 ~ Original price = £80 ~ 80 × 0.8 = 64 ✓ | Check
metric: 2.4 m = 2.4 × 100 = 240 cm ~ 3.5 litres = 3.5 × 1000 = 3500 ml ~ 2 m² = 2 × 10 000 = 20 000 cm² | Area uses a squared conversion
perimeter: Length = 4.5 m; width = 2 m ~ P = 4.5 + 2 + 4.5 + 2 | Add all four sides ~ P = 13 m
area: Parallel sides: 6 cm, 10 cm; height: 4 cm ~ A = (6 + 10) ÷ 2 × 4 ~ A = 8 × 4 = 32 cm²
compound-area: Outer rectangle: 8 cm × 6 cm ~ Missing corner: 3 cm × 2 cm ~ A = 48 − 6 = 42 cm² | Subtract the missing area
time: 2 hours 45 minutes ~ 45 ÷ 60 = 0.75 hours ~ 2 + 0.75 = 2.75 hours
timetables: 23:35 → 00:00 | 25 minutes ~ 00:00 → 00:20 | 20 minutes ~ 25 + 20 = 45 minutes
speed: Distance = 150 m; time = 30 s ~ Speed = 150 ÷ 30 ~ Speed = 5 m/s
distancegraph: (2 s, 5 m) → (6 s, 25 m) ~ Distance change = 25 − 5 = 20 m ~ Time change = 6 − 2 = 4 s ~ Speed = 20 ÷ 4 = 5 m/s
factors: 18: 1, 2, 3, 6, 9, 18 | Factors ~ 18 = 2 × 3 × 3 | Prime factors ~ 18 = 2 × 3²
powers-roots: 5² = 25 ↔ √25 = 5 ~ 3³ = 27 ↔ ∛27 = 3 ~ 1 + 2 + 3 + 4 = 10 | Fourth triangular number
hcf: 24 = 2³ × 3; 36 = 2² × 3² ~ HCF = 2² × 3 = 12 | Shared prime factors ~ LCM = 2³ × 3² = 72 | All prime factors needed
mixed: 2⅗ = (2 × 5 + 3)/5 ~ = 13/5 ~ 13 ÷ 5 = 2 remainder 3 | Change back ~ 13/5 = 2⅗
fraction-add: 2/3 + 3/4 ~ = 8/12 + 9/12 | Common denominator: 12 ~ = 17/12 = 1 5/12
fraction-algebra: x/3 + x/4 ~ = 4x/12 + 3x/12 | Common denominator: 12 ~ = 7x/12
measure: Smaller angle = 72° ~ Reflex angle = 360° − 72° ~ = 288°
shapes: Equilateral triangle: 3 equal sides ~ Cuboid: 6 faces, 12 edges, 8 vertices ~ Cylinder: circular cross-section
angles: Isosceles triangle; top angle = 38° ~ Base angles total = 180° − 38° = 142° ~ Each base angle = 142° ÷ 2 = 71° | Two equal angles
parallel: Regular hexagon: 6 sides ~ Exterior angle = 360° ÷ 6 = 60° ~ Interior angle = 180° − 60° = 120°
ratio: Red : blue = 6 : 9 = 2 : 3 | Divide both by 3 ~ Total parts = 2 + 3 = 5 ~ Red fraction = 2/5
share: £84 in the ratio 3 : 4 ~ Parts = 3 + 4 = 7 ~ One part = £84 ÷ 7 = £12 ~ Shares = 3 × £12 = £36; 4 × £12 = £48
ratio-missing: Red : blue = 2 : 5; difference = 18 ~ 5 − 2 = 3 parts ~ One part = 18 ÷ 3 = 6 ~ Red = 2 × 6 = 12; blue = 5 × 6 = 30
direct: 3 pens → £4.50 ~ 1 pen → £4.50 ÷ 3 = £1.50 ~ 8 pens → 8 × £1.50 = £12 | Same price per pen
conversion-graphs: £1 = €1.25 | Example rate ~ £20 → 20 × 1.25 = €25 ~ €45 → 45 ÷ 1.25 = £36
similarity: Small rectangle: 3 cm × 5 cm ~ Scale factor = 12 ÷ 3 = 4 ~ Other side = 5 × 4 = 20 cm
scale: 1 : 200; drawing = 3 cm ~ Real length = 3 × 200 = 600 cm ~ = 6 m ~ £35 × 1.20 = €42 | Example rate: £1 = €1.20
proportion: 4 notebooks → £6 ~ 1 notebook → £6 ÷ 4 = £1.50 ~ 10 notebooks → 10 × £1.50 = £15 | Same price per notebook
expand: −3(2x − 5) ~ = −6x + 15 | Multiply each term by −3 ~ 12x + 18 = 6(2x + 3) | Factorise: take out 6
factorise: 6x + 15 ~ = 3 × 2x + 3 × 5 | Shared factor: 3 ~ = 3(2x + 5)
double: (x + 3)(x − 2) ~ = x² − 2x + 3x − 6 | Multiply all four pairs ~ = x² + x − 6 | Collect like terms
linear: (1,5), (3,9) ~ m = (9 − 5) ÷ (3 − 1) = 2 ~ 5 = 2 × 1 + c → c = 3 | Use (1,5) ~ y = 2x + 3
curves: y = x² − 4 ~ 0 = x² − 4 → x = −2 or 2 | x-intercepts: y = 0 ~ y = 0² − 4 = −4 | y-intercept: x = 0
fraction-product: 3/4 × 2/5 = 6/20 = 3/10 ~ 2/3 ÷ 4/5 = 2/3 × 5/4 | Flip the second fraction ~ = 10/12 = 5/6
fraction-model: ½ × ¾ = ⅜ | Half of three quarters ~ ¾ ÷ ¼ = 3 | Three quarter-pieces fit
symmetry: (2,5) → mirror x = 4 → (6,5) ~ 4 − 2 = 2; 6 − 4 = 2 | Equal distances from the mirror
reflection: (2,1) → mirror x = 4 → (6,1) ~ 4 − 2 = 2; 6 − 4 = 2 | Equal distances from the mirror
volume: Triangle: base 6 cm, height 4 cm ~ Cross-section = ½ × 6 × 4 = 12 cm² ~ Volume = 12 × 10 = 120 cm³ | Prism length = 10 cm
density: Mass = 180 g; volume = 60 cm³ ~ Density = 180 ÷ 60 ~ = 3 g/cm³
fractional-equations: (x + 4)/3 = 5 ~ x + 4 = 15 | Multiply both sides by 3 ~ x = 11 | Subtract 4 from both sides
both-sides: 5x + 3 = 2x + 21 ~ 3x + 3 = 21 | Subtract 2x from both sides ~ 3x = 18 | Subtract 3 from both sides ~ x = 6 | Divide both sides by 3
inequality: −2x < 6 ~ x > −3 | Divide by −2; reverse the sign
indices-laws: x³ × x² = x⁵ | Add powers ~ x⁷ ÷ x² = x⁵ | Subtract powers; x ≠ 0 ~ (x²)³ = x⁶ | Multiply powers
powers-ten: 4.2 × 10³ = 4200 | ×1000 ~ 4.2 × 10⁻³ = 0.0042 | ÷1000
standard-read: 56 000 = 5.6 × 10⁴ ~ 0.00056 = 5.6 × 10⁻⁴ ~ 1 ≤ 5.6 < 10 | First number is between 1 and 10
data-types: Siblings: 0, 1, 2, … | Discrete: counted ~ Height: 152.3 cm | Continuous: measured ~ Sport: football, tennis, … | Categorical: labels
grouped: 140 ≤ h < 150: 2; 150 ≤ h < 160: 3 ~ Midpoints: 145, 155 ~ Total ≈ 145 × 2 + 155 × 3 = 755 ~ Mean ≈ 755 ÷ 5 = 151 cm | Estimate using midpoints
compare-data: Median: A = 12, B = 10 | A has a higher typical value ~ Range: A = 3, B = 8 | A is less spread out
histogram: 10 ≤ x < 30; frequency = 12 ~ Width = 30 − 10 = 20 ~ Density = 12 ÷ 20 = 0.6 | Bar height
quadrilaterals: Parallelogram: one angle = 68° ~ Next angle = 180° − 68° = 112° ~ Angles: 68°, 112°, 68°, 112° | Opposite angles are equal
probability: Die outcomes above 4: {5, 6} ~ P(above 4) = 2/6 = 1/3 ~ P(not above 4) = 1 − 1/3 = 2/3
experiment: Red: 18 out of 50 spins ~ Relative frequency = 18/50 = 0.36 ~ Next 100 spins: about 36 reds | Estimate, not a guarantee
sample-space: Coin × die: 2 × 6 = 12 outcomes ~ {H2, H4, H6} | Head and even ~ P(head and even) = 3/12 = 1/4
tables: Cyclists = 12; cyclists with glasses = 5 ~ P(glasses among cyclists) = 5/12 | Use the cyclists' total
frequency-tree: 30 pupils → 18 walk; 12 do not ~ 18 walkers → 10 with bags; 8 without ~ P(bag among walkers) = 10/18 = 5/9
counting: 3 shirts × 4 trousers ~ = 12 outfits
circle: Radius = 3 cm ~ C = 2πr = 2 × π × 3 = 6π cm ~ A = πr² = π × 3² = 9π cm²
circle-parts: Semicircle: radius = 4 cm ~ Curved edge = ½ × 2π × 4 = 4π cm ~ Perimeter = 4π + 8 cm | Include the diameter
cylinder: Radius = 3 cm; height = 8 cm ~ Base area = π × 3² = 9π cm² ~ Cylinder = 9π × 8 = 72π cm³ ~ Cone = 72π ÷ 3 = 24π cm³ | Same base and height
pie: 15 out of 60 pupils walk ~ Fraction = 15/60 = 1/4 ~ Sector = 1/4 × 360° = 90°
stem: 2 ¦ 1 4 4 8 | Key: 2 ¦ 4 = 24 ~ 21, 24, 24, 28 ~ Median = (24 + 24) ÷ 2 = 24 ~ Range = 28 − 21 = 7
number-sets: −4 = −4/1 | Integer and rational ~ 0.125 = 1/8 | Rational ~ √2 | Irrational ~ √9 = 3 | Rational
repeated-change: £200 × 1.1 = £220 | First 10% rise ~ £220 × 1.1 = £242 | Second 10% rise ~ 42 ÷ 200 × 100 = 21% | Total increase
interest: £300 × 0.04 = £12 | Simple interest per year ~ £300 + 3 × £12 = £336 | After 3 years ~ £300 × 1.04³ ≈ £337.46 | Compound interest instead
nets-surface: Cuboid: 4 cm × 3 cm × 2 cm ~ Faces: 4 × 3 = 12; 4 × 2 = 8; 3 × 2 = 6 ~ Area = 2(12 + 8 + 6) | Two of each face ~ = 52 cm²
solid-volume: Cone: radius = 3 cm; height = 8 cm ~ V = ⅓ × π × 3² × 8 ~ V = 24π cm³
rearrange: v = u + at ~ v − u = at | Subtract u ~ t = (v − u)/a | Divide by a; a ≠ 0
recurring: x = 0.272727… ~ 100x = 27.272727… | Multiply by 100 ~ 99x = 27 | Subtract the first line ~ x = 27/99 = 3/11
flow-rates: In: 8 litres/min; out: 3 litres/min ~ Net rate = 8 − 3 = 5 litres/min ~ Increase = 5 × 6 = 30 litres | After 6 minutes
compound-units: 10 m/s × 3600 = 36 000 m/h ~ 36 000 ÷ 1000 = 36 km/h
velocitygraph: 0 → 12 m/s in 6 s ~ Acceleration = 12 ÷ 6 = 2 m/s² ~ Distance = ½ × 6 × 12 = 36 m | Triangle under the graph
standard-calc: (3 × 10⁵) + (4 × 10⁴) ~ = (3 × 10⁵) + (0.4 × 10⁵) | Match the powers ~ = 3.4 × 10⁵ | Add the first numbers
surds: √72 = √(36 × 2) = 6√2 ~ 3/√5 = (3 × √5)/(√5 × √5) ~ = 3√5/5
money-bank: £45 − £60 = −£15 | Payment ~ −£15 + £25 = £10 | Deposit
money-pay: 6 × £12 = £72 | Gross pay ~ £72 − £8 = £64 | Net pay after deductions ~ £40 × 1.20 = £48 | Price including 20% VAT
money-budget: Income = £160 ~ Spending = £90 + £45 = £135 ~ Surplus = £160 − £135 = £25
money-save: 750 g = 0.75 kg; price = £3 ~ £3 ÷ 0.75 = £4 per kg ~ £4 < £4.20 per kg | First pack is cheaper per kg
money-borrow: Loan = £600; fee = £15 ~ Repayment = 12 × £55 + £15 = £675 ~ Extra cost = £675 − £600 = £75
money-overseas: £150 × 1.20 = €180 | Example rate: £1 = €1.20 ~ €180 − €6 = €174 | Deduct the fee
money-insurance: 12 × £9 = £108 | Yearly premium ~ £500 − £100 = £400 | Covered loss minus excess
line-equation: (0,−2), (3,4) ~ m = (4 − (−2)) ÷ (3 − 0) = 2 ~ c = −2 | Read the y-intercept ~ y = 2x − 2
graph-inequalities: y > x + 1 ~ y = x + 1 | Draw a dashed boundary ~ (0,0): 0 > 1 ✗ | Test a point ~ Shade above the line | Exclude the boundary
perpendicular: m = 2 ~ Perpendicular gradient = −1/2 ~ 2 × (−1/2) = −1 ✓ | Check
construct-triangle: AB = 6 cm | Draw the base ~ A: radius 5 cm; B: radius 4 cm | Draw two arcs ~ C = arc crossing | Join A to C and B to C
bisectors: AB = 8 cm; compass radius = 5 cm ~ Arc centres: A and B | Equal arcs above and below ~ Crossings → straight line | Midpoint at 90°
congruence: Triangle A: 4, 5, 6 cm ~ Triangle B: 4, 5, 6 cm ~ A ≅ B (SSS) | Three matching sides ~ 40°, 60°, 80° only → similar | Angles do not fix size
similar-triangles: Small: base 4 cm, height 3 cm ~ Scale factor = 10 ÷ 4 = 2.5 ~ New height = 3 × 2.5 = 7.5 cm
quadratic-solve: x² + 5x + 6 = 0 ~ (x + 2)(x + 3) = 0 | Factorise ~ x + 2 = 0 or x + 3 = 0 ~ x = −2 or x = −3
algebra-extend: (x + 1)(x + 2)(x + 3) ~ = (x² + 3x + 2)(x + 3) ~ = x³ + 3x² + 3x² + 9x + 2x + 6 ~ = x³ + 6x² + 11x + 6 | Collect like terms
pythagoras: Shorter sides: 6 cm, 8 cm ~ c² = 6² + 8² ~ c² = 36 + 64 = 100 ~ c = √100 = 10 cm
pythagoras-check: 5² + 12² = 25 + 144 = 169 ~ 13² = 169 ✓ | Right-angled triangle ~ (1,2) → (6,14): gaps 5 and 12 ~ Distance = √(5² + 12²) = 13
trig: Angle = 30°; hypotenuse = 10 cm ~ sin 30° = opposite/10 ~ Opposite = 10 × sin 30° ~ = 5 cm
trig-exact: Horizontal distance = 20 m; angle = 45° ~ Height = 20 × tan 45° | Above eye level ~ = 20 × 1 = 20 m
graph-families: y = 2ˣ: (−1,0.5), (0,1), (1,2), (2,4) ~ y = 1/x: (−2,−0.5), (−1,−1), (1,1), (2,0.5) ~ y = x³: (−2,−8), (−1,−1), (0,0), (1,1), (2,8)
sets: A only: 8; both: 4; B only: 5; neither: 3 ~ A ∩ B: 4 | Both ~ A ∪ B: 8 + 4 + 5 = 17 | Either or both ~ P(A) = (8 + 4)/20 = 3/5
expected: P(4) = 1/6 ~ Expected 4s = 180 × 1/6 = 30 | In 180 rolls; not guaranteed
independent: P(H then H) = ½ × ½ = ¼ | Independent coin tosses ~ P(1 or 6) = 1/6 + 1/6 = 1/3 | One die roll: cannot get both
enlargement: (2,1), centre (0,0), factor 3 ~ (2 × 3, 1 × 3) ~ Image = (6,3)
rotation: (3,1) → (−1,3) | 90° anticlockwise about (0,0) ~ (x,y) → (−x,−y) | 180° about (0,0)
translation: (−1,4) + (3,−2) | 3 right, 2 down ~ (−1 + 3, 4 − 2) ~ Image = (2,2)
transform-series: (1,2) → (4,2) → (−4,2) | Right 3; reflect in y-axis ~ (1,2) → (−1,2) → (2,2) | Reflect first; then right 3 ~ (−4,2) ≠ (2,2) | Order matters
simultaneous: x + y = 9; x − y = 3 ~ 2x = 12 | Add the equations ~ x = 6 ~ y = 9 − 6 = 3
simultaneous-adjust: 2x + y = 11; 3x + 2y = 19 ~ 4x + 2y = 22 | Double the first equation ~ x = 3 | Subtract the second equation ~ y = 11 − 2 × 3 = 5
trig-angle: Opposite = 3 cm; adjacent = 4 cm ~ tan θ = 3/4 ~ θ = tan⁻¹(0.75) ~ θ ≈ 36.9° | Calculator in degrees
trig-choice: c = √(5² + 12²) = 13 | Two shorter sides known ~ Opposite = 10 × sin 30° = 5 | Hypotenuse and angle known
quadratic-sequence: 3, 8, 15, 24 | Gaps: 5, 7, 9 ~ 3−1, 8−4, 15−9, 24−16 | Subtract n² ~ 2, 4, 6, 8 = 2n ~ Rule = n² + 2n
"""

EXAMPLES = {}
for line in DATA.strip().splitlines():
    key, raw = line.split(': ', 1)
    assert key not in EXAMPLES, key
    rows = []
    for row in raw.split(' ~ '):
        work, _, note = row.partition(' | ')
        rows.append(dict(work=work, note=note))
    EXAMPLES[key] = rows
