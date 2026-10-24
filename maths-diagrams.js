/* Small, labelled teaching diagrams. Data and formulae are fixed examples, never student code. */
(()=>{'use strict';
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const text=(x,y,s,size=26,anchor='middle')=>`<text x="${x}" y="${y}" font-size="${size}" text-anchor="${anchor}">${esc(s)}</text>`;
const line=(x1,y1,x2,y2,cls='',extra='')=>`<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" class="${cls}" ${extra}/>`;
const rect=(x,y,w,h,cls='')=>`<rect x="${x}" y="${y}" width="${w}" height="${h}" class="${cls}"/>`;
const circle=(x,y,r,cls='')=>`<circle cx="${x}" cy="${y}" r="${r}" class="${cls}"/>`;
function svg(label,body){return `<svg viewBox="0 0 520 300" role="img" aria-label="${esc(label)}">${body}</svg>`;}
function figure(body,caption){return `<figure class="ks-maths-diagram">${body}<figcaption>${esc(caption)}</figcaption></figure>`;}
const table=(headers,rows)=>`<div class="ks-table-scroll"><table><thead><tr>${headers.map(s=>`<th scope="col">${esc(s)}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${row.map(s=>`<td>${esc(s)}</td>`).join('')}</tr>`).join('')}</tbody></table></div>`;
const flow=items=>`<ol class="ks-maths-flow" style="--flow-count:${items.length}">${items.map(s=>`<li>${esc(s)}</li>`).join('')}</ol>`;
const equation=rows=>`<ol class="ks-equation-steps">${rows.map(([work,why])=>`<li><strong>${esc(work)}</strong><span>${esc(why)}</span></li>`).join('')}</ol>`;
function fraction(n,d,label){let g='';for(let i=0;i<d;i++)g+=rect(50+i*420/d,95,420/d,72,i<n?'filled':'');g+=text(260,65,label,28)+text(260,218,`${n} shaded parts out of ${d} equal parts`,26);return svg(label,g);}
function numberline({min=-6,max=6,from=-4,to=3,label='−4 + 7 = 3',inequality=false}={}){const x=v=>45+(v-min)/(max-min)*430;let g=line(35,180,485,180);for(let v=min;v<=max;v++){g+=line(x(v),172,x(v),188);if(v===0||v===min||v===max||v%3===0)g+=text(x(v),222,v,23);}if(inequality){g+=line(x(from),180,x(to),180,'heavy')+circle(x(from),180,8,'filled');g+=`<path class="heavy" d="M${x(to)-10} 172l16 8-16 8Z"/>`;}else{g+=`<path class="accent" d="M${x(from)} 145 Q${(x(from)+x(to))/2} 35 ${x(to)} 145" fill="none"/><path class="accent" d="M${x(to)-8} 135l8 12 7-12" fill="none"/>`+circle(x(from),180,5,'filled')+circle(x(to),180,5,'filled');}return svg(label,g+text(260,45,label,27));}
function triangle(kind='area'){let g;if(kind==='trig'){g=`<path class="soft" d="M80 240H426.4L80 40Z"/>`+line(80,220,100,220)+line(100,220,100,240)+text(42,145,'5',28)+text(255,278,'Adjacent side',23)+text(300,112,'Hypotenuse 10',23)+text(366,228,'30°',24)+text(115,25,'Opposite side',23);}else if(kind==='pythagoras'){g=`<path class="soft" d="M120 240H360L120 60Z"/>`+line(120,220,140,220)+line(140,220,140,240)+text(78,150,'6 cm')+text(245,280,'8 cm')+text(290,135,'10 cm');}else if(kind==='angles'){g=`<path class="soft" d="M70 240H450L280 45Z"/>`+text(126,223,'48°')+text(391,223,'67°')+text(279,107,'?');}else{g=`<path class="soft" d="M65 238H455L255 45Z"/>`+line(255,45,255,238,'dash')+line(255,218,275,218)+line(275,218,275,238)+text(260,280,'Base 12 cm')+text(335,158,'Height 7 cm',23);}return svg('Labelled triangle',g);}
function axes({xmin=-4,xmax=4,ymin=-4,ymax=8,xlabel='x',ylabel='y'}={}){const X=x=>65+(x-xmin)/(xmax-xmin)*390,Y=y=>245-(y-ymin)/(ymax-ymin)*195;let g='';for(let x=xmin;x<=xmax;x++)g+=line(X(x),50,X(x),245,'grid');for(let y=ymin;y<=ymax;y+=2)g+=line(65,Y(y),455,Y(y),'grid');g+=line(65,Y(0),465,Y(0))+line(X(0),35,X(0),250);for(let x=xmin;x<=xmax;x+=2)g+=text(X(x),275,x,24);for(let y=ymin;y<=ymax;y+=2)if(y!==0)g+=text(52,Y(y)+7,y,24,'end');g+=text(492,Y(0)+5,xlabel,23)+text(X(0)+15,25,ylabel,23);return{g,X,Y};}
function graph(kind){let a,g;if(kind==='distance'||kind==='velocity'){a=axes({xmin:0,xmax:6,ymin:0,ymax:12,xlabel:'s',ylabel:kind==='distance'?'m':'m/s'});g=a.g;if(kind==='velocity')g+=`<path class="soft" d="M${a.X(0)} ${a.Y(0)}L${a.X(6)} ${a.Y(12)}L${a.X(6)} ${a.Y(0)}Z"/>`;g+=line(a.X(0),a.Y(0),a.X(6),a.Y(12),'heavy');}else if(kind==='scatter'){a=axes({xmin:0,xmax:6,ymin:0,ymax:12,xlabel:'A',ylabel:'B'});g=a.g+[[1,3],[2,4],[3,7],[4,7],[5,10]].map(([x,y])=>circle(a.X(x),a.Y(y),5,'filled')).join('');g+=line(a.X(.5),a.Y(2),a.X(5.5),a.Y(11),'dash');}else{a=axes();g=a.g;if(kind==='curves'){const pts=[];for(let x=-3.3;x<=3.3;x+=.1)pts.push(`${a.X(x)},${a.Y(x*x-4)}`);g+=`<polyline class="accent" points="${pts.join(' ')}" fill="none"/>`;}else if(kind==='symmetry'){g+=line(a.X(0),40,a.X(0),245,'dash')+circle(a.X(-3),a.Y(4),6,'filled')+circle(a.X(3),a.Y(4),6,'other');g+=line(a.X(-3),a.Y(4),a.X(3),a.Y(4),'dash')+text(a.X(-3),a.Y(4)-17,'(−3, 4)',21)+text(a.X(3),a.Y(4)-17,'(3, 4)',21);}else if(kind==='coordinates'){g+=line(a.X(-2),a.Y(0),a.X(2),a.Y(8),'accent')+circle(a.X(-2),a.Y(0),5,'filled')+circle(a.X(2),a.Y(8),5,'filled')+circle(a.X(0),a.Y(4),7,'other')+text(a.X(0)+95,a.Y(4)+8,'Midpoint (0, 4)',21);}else{g+=line(a.X(-2),a.Y(-1),a.X(2),a.Y(7),'heavy');g+=line(a.X(0),a.Y(3),a.X(2),a.Y(3),'dash')+line(a.X(2),a.Y(3),a.X(2),a.Y(7),'dash')+text(a.X(1),a.Y(3)+29,'Across 2',20)+text(a.X(2)+9,a.Y(5),'Up 4',20,'start');}}return svg('Example graph with labelled axes',g);}
function rectangle(){return svg('A 4.5 m by 2 m rectangle',rect(90,75,340,150,'soft')+text(260,50,'4.5 m')+text(52,160,'2 m')+text(260,278,'Around the outside: perimeter',23));}
function cuboid(){return svg('Cuboid with three labelled dimensions',`<path class="soft" d="M100 110H360V240H100ZM100 110l65-55h260l-65 55M360 240l65-55V55"/>`+line(100,240,165,185,'dash')+line(165,185,425,185,'dash')+line(165,185,165,55,'dash')+text(230,280,'8 cm')+text(405,236,'5 cm')+text(62,180,'3 cm'));}
function circleDiagram(){return svg('Radius and diameter of a circle',circle(260,145,95,'soft')+line(165,145,355,145,'accent')+line(260,145,260,50,'heavy')+circle(260,145,4,'filled')+text(320,95,'r = 3',23)+text(260,185,'Diameter = 6',24)+text(260,280,'Circumference goes around the edge',23));}
function cones(){return svg('A cylinder and cone with the same base and height',`<ellipse class="soft" cx="140" cy="225" rx="70" ry="22"/><path class="soft" d="M70 225V65H210V225"/><ellipse class="soft" cx="140" cy="65" rx="70" ry="22"/><path class="soft" d="M310 225L380 65L450 225Z"/><ellipse class="soft" cx="380" cy="225" rx="70" ry="22"/>`+line(380,65,380,225,'dash')+text(140,280,'Cylinder: 3 parts',23)+text(380,280,'Cone: 1 part',23)+text(140,150,'Same r',24)+text(405,148,'h',24));}
function pie(){return svg('A quarter of a full pie chart',circle(260,145,100,'soft')+`<path class="filled" d="M260 145V45A100 100 0 0 1 360 145Z"/>`+text(295,110,'90°',27)+text(260,285,'¼ of 360° = 90°',26));}
function histogram(){const X=x=>65+x*9.5,Y=y=>245-y*190;let g=line(65,245,455,245)+line(65,45,65,245);for(const x of [0,10,20,30,40])g+=text(X(x),277,x,22);for(const y of [0,.3,.6,.9])g+=text(52,Y(y)+7,y,24,'end');g+=rect(X(10),Y(.6),190,.6*190,'soft')+rect(X(30),Y(.9),95,.9*190,'other')+text(260,25,'Frequency density',25)+text(X(20),Y(.6)+35,'12',26)+text(X(35),Y(.9)+35,'9',26);return svg('Histogram: unequal widths and frequency represented by area',g);}
function protractor(){let g=line(75,245,445,245);for(let deg=0;deg<=180;deg+=10){const a=deg*Math.PI/180,x=260+160*Math.cos(a),y=245-160*Math.sin(a);g+=line(x,y,260+145*Math.cos(a),245-145*Math.sin(a));if(deg%30===0)g+=text(260+190*Math.cos(a),250-190*Math.sin(a),deg+'°',21);}g+=`<path d="M100 245A160 160 0 0 1 420 245" fill="none"/>`+line(260,245,340,106,'heavy')+circle(260,245,5,'filled');return svg('A protractor read from zero on the right; the ray shows 60 degrees',g);}
function factorVenn(){return svg('Prime factors of 24 and 36 in a Venn diagram',`<ellipse class="soft" cx="200" cy="150" rx="130" ry="100"/><ellipse class="soft" cx="320" cy="150" rx="130" ry="100"/>`+text(130,45,'24')+text(390,45,'36')+text(150,155,'2')+text(370,155,'3')+text(260,125,'2 × 2')+text(260,165,'× 3')+text(260,290,'Shared part: HCF = 12',24));}
function counters(){let g='';for(let i=0;i<10;i++)g+=circle(90+(i%5)*85,90+Math.floor(i/5)*90,23,i<3?'counter-red':i<8?'counter-blue':'counter-green')+text(90+(i%5)*85,98+Math.floor(i/5)*90,i<3?'R':i<8?'B':'G',22);return svg('Ten counters: three red-group, five blue-group and two green-group',g+text(260,260,'3 red · 5 blue · 2 green',24));}
const D={};function add(keys,caption,body){for(const key of keys.split(' '))D[key]={caption,body};}
add('sequence','The terms gain four tiles each time.',()=>{let g='';for(let row=0;row<3;row++){const n=3+row*4;g+=text(65,65+row*85,'Term '+(row+1),22);for(let i=0;i<n;i++)g+=rect(145+i*28,43+row*85,23,23,'filled');g+=text(485,65+row*85,n,24);}return svg('Tile rows with 3, 7 and 11 tiles',g);});
add('nonlinear','The first differences change, but the second differences stay at 2.',()=>table(['Terms','First differences','Second differences'],[['1, 4, 9, 16','3, 5, 7','2, 2']]));
add('nth','The four-times table needs 3 added to match these terms.',()=>table(['Position n','4n','4n + 3'],[[1,4,7],[2,8,11],[3,12,15],[4,16,19]]));
add('quadratic-sequence','Subtract n² to reveal the simpler pattern 2n.',()=>table(['Position','Term','Term − n²'],[[1,3,2],[2,8,4],[3,15,6],[4,24,8]]));
add('function','Follow the operations from left to right. Undo them in reverse order.',()=>flow(['Input 6','×3','+4','Output 22']));
add('notation','Brackets change what is squared.',()=>table(['Expression','When a = 4','Value'],[['3a²','3 × 4²',48],['(3a)²','12²',144]]));
add('substitute','Replace letters with values, keeping a negative value in brackets.',()=>equation([['x² − 4y','x = −3, y = 2'],['(−3)² − 4 × 2','Replace the letters'],['9 − 8 = 1','Powers, then multiply, then subtract']]));
add('like','Collect matching letter parts. Keep their signs.',()=>table(['a terms','b terms','Simplified'],[['5a − 2a','3b + b','3a + 4b']]));
add('equation','Each operation is applied to both sides.',()=>equation([['3x + 5 = 26','Subtract 5 from both sides'],['3x = 21','Divide both sides by 3'],['x = 7','Check: 3 × 7 + 5 = 26']]));
add('balance','Subtract the same amount from both sides to keep the equation balanced.',()=>equation([['x + 8 = 19','Subtract 8 from both sides'],['x = 11','The unknown is now alone'],['11 + 8 = 19','Check the original equation']]));
add('both-sides','Move letter terms by applying the same subtraction on both sides.',()=>equation([['5x + 3 = 2x + 21','Subtract 2x from both sides'],['3x + 3 = 21','Subtract 3, then divide by 3'],['x = 6','Both original sides equal 33']]));
add('rearrange','Make t stand alone by undoing addition, then multiplication.',()=>equation([['v = u + at','Subtract u'],['v − u = at','Divide the whole left side by a'],['t = (v − u) ÷ a','This needs a ≠ 0']]));
add('expand','The outside factor multiplies every term in the bracket.',()=>table(['×','2x','−5'],[['−3','−6x','+15']]));
add('double','A grid shows all four products before you collect like terms.',()=>table(['×','x','−2'],[['x','x²','−2x'],['+3','3x','−6']]));
add('place','A zero holds a place. Add trailing zeros to compare matching columns.',()=>table(['Number','Tenths','Hundredths','Thousandths'],[['0.407',4,0,7],['0.470',4,7,0]]));
add('round','Keep two significant figures. The next digit decides whether to round up.',()=>flow(['0.006847','Keep 6 and 8','Next digit: 4','0.0068']));
add('estimate','For rounding to the nearest centimetre, this interval includes 11.5 but excludes 12.5.',()=>table(['Lower end','Rounded value','Upper end'],[['11.5 cm included','12 cm','12.5 cm excluded']]));
add('add','Line up decimal places before subtracting.',()=>table(['Tens','Units','·','Tenths','Hundredths'],[[1,3,'·',7,0],['−',8,'·',4,6],['=',5,'·',2,4]]));
add('multiply','Multiply whole numbers, then restore three decimal places.',()=>flow(['2.4 × 0.35','24 × 35 = 840','÷1000','0.84']));
add('divide','Multiplying both numbers by ten keeps the answer the same.',()=>equation([['6.3 ÷ 0.3','Multiply both numbers by 10'],['63 ÷ 3','Now the divisor is a whole number'],['21','Check: 21 × 0.3 = 6.3']]));
add('order','Keep operations at the same level in left-to-right order.',()=>flow(['18 ÷ 3 × 2','6 × 2','12']));
add('directed','Start at −4 and move seven steps right to reach 3.',()=>numberline());
add('negative-products','These sign rules apply to multiplying or dividing two numbers.',()=>table(['First sign','Second sign','Answer sign'],[['+','+','+'],['−','−','+'],['+','−','−'],['−','+','−']]));
add('mean','Order the values to find the median. Do not remove repeats.',()=>table(['Ordered values','Mean','Median / mode','Range'],[['2, 3, 3, 8','16 ÷ 4 = 4','3 / 3','8 − 2 = 6']]));
add('frequency','Multiply each value by how often it occurs.',()=>table(['Value','Frequency','Value × frequency'],[[1,2,2],[2,5,10],[3,3,9],['Total',10,21]]));
add('charts','A half-symbol counts as half the amount in the key.',()=>table(['Key','Two symbols','Half a symbol','Total'],[['1 symbol = 4 pupils',8,2,10]]));
add('scatter','These example points rise overall. The dashed line follows the main pattern.',()=>graph('scatter'));
add('coordinates','The midpoint of (−2, 0) and (2, 8) is (0, 4). Average x and y separately.',()=>graph('coordinates'));
add('fdp','The same amount can be shown as a fraction, decimal and percentage.',()=>fraction(3,8,'3/8 = 0.375 = 37.5%'));
add('equivalent','Splitting each quarter in half makes eighths without changing the shaded amount.',()=>table(['Fraction','Multiply top and bottom','Equivalent fraction'],[['3/4','×2','6/8']]));
add('fraction-amount','Split the whole into five equal parts. Three parts are shaded.',()=>fraction(3,5,'3/5 of 80: each part is 16'));
add('percent-amount','Build 15% from 10% and 5%.',()=>table(['Share of £80','Amount'],[['10%','£8'],['5%','£4'],['15%','£12']]));
add('change','Always compare the change with the original amount.',()=>flow(['Original £50','Increase £15','15 ÷ 50 × 100','30% increase']));
add('reverse','The final amount is 80% of the original, so divide by 0.8.',()=>equation([['Original × 0.8 = £64','After a 20% reduction'],['Original = £64 ÷ 0.8','Undo the multiplier'],['Original = £80','Check: £80 × 0.8 = £64']]));
add('perimeter','Add every outside edge once.',rectangle);
add('area','The dashed height is at right angles to the base. This drawing is not to scale.',()=>triangle('area'));
add('time','Minutes are parts of sixty, not parts of one hundred.',()=>flow(['45 minutes','45 ÷ 60 hours','0.75 hours']));
add('speed','Check the units before using the relationship.',()=>flow(['Distance in m','÷ time in s','Speed in m/s']));
add('distancegraph','This distance rises 12 m in 6 seconds, so speed is 2 m/s.',()=>graph('distance'));
add('factors','Split 18 into prime factors, then write repeated factors as powers.',()=>flow(['18','2 × 9','2 × 3 × 3','2 × 3²']));
add('hcf','Use the shared prime factors for HCF. Use every region once for LCM.',factorVenn);
add('fraction-add','The parts must be the same size before you combine them.',()=>equation([['2/3 + 3/4','Use denominator 12'],['8/12 + 9/12','Now both fractions count twelfths'],['17/12 = 1 5/12','Add the numerators']]));
add('fraction-algebra','Use exactly the same common-denominator idea with letters.',()=>equation([['x/3 + x/4','Use denominator 12'],['4x/12 + 3x/12','Multiply top and bottom'],['7x/12','Combine the numerators']]));
add('angles','The three inside angles total 180°. The drawing is not to scale.',()=>triangle('angles'));
add('measure','Start reading at zero on the arm you lined up. This example shows 60°.',protractor);
add('ratio','Each box is one equal ratio unit: two red and three blue.',()=>`<div class="ks-ratio-units" role="img" aria-label="Five equal boxes: two red labelled R and three blue labelled B">${['R','R','B','B','B'].map(s=>`<span class="${s==='R'?'ratio-a':'ratio-b'}">${s}</span>`).join('')}</div>`);
add('share','£84 shared in the ratio 3:4 gives seven equal units of £12: shares £36 and £48.',()=>'<div class="ks-ratio-units" role="img" aria-label="Seven equal boxes, each worth 12 pounds. Three belong to one share and four to the other.">'+Array.from({length:7},(_,i)=>'<span class="'+(i<3?'ratio-a':'ratio-b')+'">12</span>').join('')+'</div>');
add('proportion','Find the cost for one before scaling to the new number.',()=>table(['Notebooks','Cost'],[[4,'£6'],[1,'£1.50'],[10,'£15']]));
add('scale','Convert the real length into the unit requested after scaling.',()=>flow(['3 cm on plan','×200','600 cm in reality','6 m']));
add('linear','This line goes up 4 while moving across 2. Its gradient is 2.',()=>graph('linear'));
add('perpendicular','Parallel gradients match. Perpendicular non-vertical gradients multiply to −1.',()=>table(['First gradient','Parallel gradient','Perpendicular gradient'],[[2,2,'−1/2'],['−4','−4','1/4']]));
add('fraction-product','Turn over only the divisor when changing division to multiplication.',()=>flow(['2/3 ÷ 4/5','2/3 × 5/4','10/12','5/6']));
add('symmetry','The y-axis is the mirror line. Both points are three units away.',()=>graph('symmetry'));
add('volume','Multiply the three lengths for a cuboid. The drawing is not to scale.',cuboid);
add('density','Keep the mass and volume units together in the answer.',()=>flow(['Mass 180 g','÷ volume 60 cm³','Density 3 g/cm³']));
add('inequality','For x ≥ −3, a filled circle includes −3 and the arrow goes towards larger numbers.',()=>numberline({min:-6,max:6,from:-3,to:6,label:'x ≥ −3',inequality:true}));
add('parallel','An interior angle and its exterior partner add to 180°.',()=>table(['Regular shape','Exterior angle','Interior angle'],[['Hexagon','360° ÷ 6 = 60°','180° − 60° = 120°']]));
add('probability','There are five non-blue counters out of ten, so P(not blue) = 1/2.',counters);
add('tables','If choosing a cyclist, the total is 12, not the whole survey.',()=>table(['','Glasses','No glasses','Total'],[['Cyclists',5,7,12],['Not cyclists',7,11,18],['Total',12,18,30]]));
add('circle','The diameter is twice the radius. Units here are centimetres.',circleDiagram);
add('cylinder','With the same radius and perpendicular height, the cone volume is one third of the cylinder.',cones);
add('pie','One quarter of the total takes one quarter of the full turn.',pie);
add('indices','The denominator of the power gives the root; the numerator gives the next power.',()=>flow(['8 to power 2/3','Cube root: 2','Square: 2²','4']));
add('standard','The first number must be at least 1 and less than 10 for a positive value.',()=>equation([['12 × 10⁸','12 is too large'],['1.2 × 10 × 10⁸','Make 12 into 1.2 × 10'],['1.2 × 10⁹','Now it is in standard form']]));
add('surds','Take the square-number factor outside the root.',()=>flow(['√72','√(36 × 2)','√36 × √2','6√2']));
add('counting','Each first choice pairs with every second choice.',()=>table(['','Trousers 1','Trousers 2','Trousers 3'],[['Top A','A1','A2','A3'],['Top B','B1','B2','B3'],['Top C','C1','C2','C3'],['Top D','D1','D2','D3']]));
add('recurring','Subtract the aligned repeating tails to leave a whole-number equation.',()=>equation([['100x = 27.272727…','x = 0.272727…'],['100x − x = 27','The repeating tails cancel'],['x = 27/99 = 3/11','Divide by 99 and simplify']]));
add('pythagoras','The square on the longest side equals the sum of the other two squares.',()=>triangle('pythagoras'));
add('trig trig-exact','Choose the angle before naming opposite and adjacent. This 30° triangle has sin 30° = 5/10.',()=>triangle('trig'));
add('histogram','The wider bar can contain more data even when its height is lower. Numbers inside bars are frequencies.',histogram);
add('stem','The key says how to read each value. Repeated leaves stay in the list.',()=>table(['Stem','Leaves'],[[1,'4  7'],[2,'1  4  4  8'],['Key','2 ¦ 4 = 24']]));
add('velocitygraph','The shaded area is ½ × 6 × 12 = 36 m. Velocity stays positive here.',()=>graph('velocity'));
add('curves','For y = x² − 4, the curve meets the x-axis at −2 and 2.',()=>graph('curves'));
function html(key){const d=D[key];return d?figure(d.body(),d.caption):'';}
window.KS3MathsDiagrams={html,keys:Object.keys(D)};
})();
