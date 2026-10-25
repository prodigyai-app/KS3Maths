"""Department route, checked against the supplied teaching folders (25 Oct 2026).

Y7/Y8: numbered lesson files; 2026–27 schemes fill missing folders.
Y9: Year 9 Combined SOW.xlsx, Y9 Combined (H+F), not the separate
Higher Breakdown or Foundation GCSE tabs. Revision lessons consolidate
several teaching lessons; these are not one-to-one copies of the slides.
The White Rose representation/content bank stays independent of this order.
"""
from white_rose import PLAN as WHITE_ROSE_PLAN
from content import UNITS

# Stable unit numbers, ordered concept keys, extra challenge keys.
Y7 = [
 ('sequence nonlinear nth','nth'),
 ('function notation substitute',''),
 ('balance like equation',''),
 ('place round-dp standard round','round'),
 ('add multiply divide order',''),
 ('mean missing-average frequency','frequency'),
 ('round estimate',''),
 ('charts bar-charts first-quadrant scatter time-series graph-relationships coordinates','coordinates'),
 ('fraction-order fdp equivalent',''),
 ('directed zero-pairs negative-products order indices','indices'),
 ('fraction-amount fraction-whole percent-amount change reverse',''),
 ('metric perimeter area compound-area',''),
 ('time timetables speed distancegraph',''),
 ('factors powers-roots hcf indices','indices'),
 ('equivalent mixed fraction-add fraction-algebra',''),
 ('angles parallel measure shapes',''),
]
Y8 = [
 ('ratio share ratio-missing',''),
 ('direct conversion-graphs proportion similarity scale metric','metric'),
 ('notation like substitute factorise expand double','double'),
 ('coordinates linear curves','curves'),
 ('fraction-model fraction-product fraction-algebra',''),
 ('symmetry reflection',''),
 ('shapes area volume metric density',''),
 ('equation fractional-equations both-sides inequality',''),
 ('percent-amount change reverse',''),
 ('data-types mean scatter compare-data frequency grouped histogram','histogram'),
 ('angles quadrilaterals parallel',''),
 ('probability experiment sample-space tables frequency-tree counting','counting'),
 ('circle circle-parts cylinder area',''),
 ('charts bar-charts pie time-series stem',''),
]
Y9 = [
 ('add multiply divide directed round estimate counting',''),
 ('negative-products indices order',''),
 ('factors hcf number-sets',''),
 ('powers-ten standard-read standard standard-calc surds',''),
 ('notation like substitute expand factorise double fraction-algebra quadratic-solve algebra-extend','quadratic-solve algebra-extend'),
 ('equation fractional-equations both-sides substitute rearrange inequality','inequality'),
 ('inequality',''),
 ('nth quadratic-sequence nonlinear','quadratic-sequence'),
 ('equivalent fraction-add fraction-product fraction-amount recurring','recurring'),
 ('fdp change reverse repeated-change interest',''),
 ('ratio share ratio-missing direct conversion-graphs proportion scale',''),
 ('angles parallel',''),
 ('pythagoras pythagoras-check trig trig-exact','trig-exact'),
 ('mean frequency stem',''),
 ('charts pie histogram',''),
 ('scatter',''),
 ('coordinates time speed distancegraph flow-rates compound-units velocitygraph',''),
 ('linear line-equation perpendicular graph-inequalities','graph-inequalities'),
 ('curves graph-families',''),
]

# Preserve the concept inventory of each existing unit: no deleted routes.
old = {p[2]: p for p in WHITE_ROSE_PLAN}
legacy = {}
for year in (7,8,9):
 for n, (_, title, keys) in enumerate((u for u in UNITS if u[0] == year),1):
  uid=f'y{year}-unit-{n:02}'
  legacy[uid]=(title,keys)

PLAN=[]
for year, rows in ((7,Y7),(8,Y8),(9,Y9)):
 for n,(keys,extra) in enumerate(rows,1):
  uid=f'y{year}-unit-{n:02}'
  previous=old.get(uid)
  inventory=set((previous[4] if previous else legacy[uid][1]).split()) | set(legacy[uid][1].split())
  # New concept pages are outside this navigation-only change.
  keys=' '.join(k for k in keys.split() if k in inventory)
  assert set(keys.split())==inventory,(uid, inventory-set(keys.split()))
  term=('Autumn' if n<=6 else 'Spring' if n<=12 else 'Summer') if year==7 else ('Autumn' if n<=6 else 'Spring' if n<=10 else 'Summer') if year==8 else ('GCSE Unit 1' if n<=4 else 'GCSE Unit 2' if n<=8 else 'GCSE Unit 3' if n<=11 else 'GCSE Unit 4' if n<=13 else 'GCSE Unit 5' if n<=16 else 'GCSE Unit 6')
  PLAN.append((year,term,uid,legacy[uid][0],keys,extra))

EXTRAS=[(p[0],'Extra revision',p[2],p[3],p[4],p[4]) for p in WHITE_ROSE_PLAN if '-wr-' in p[2]]
OPTIONAL=set()
CHECKED='2026-10-25'
VERSION='Department teaching order with White Rose-style representations'
SOURCES={7:'Y7 SOW NEW 2026-2027.xlsx and numbered Year 7 lesson folders',8:'Y8 SOW NEW 2026-2027.xlsx and numbered Year 8 lesson folders',9:'Year 9 Combined SOW.xlsx · Y9 Combined (H+F)'}
