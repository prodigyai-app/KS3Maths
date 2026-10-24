"""Rebuild public course data using only original, checked source files in this repository."""
from pathlib import Path
import json,copy,re,hashlib
from content import K,UNITS
from papers import P
from route_papers import COVERAGE
from revision import R
from white_rose import PLAN,OPTIONAL,VERSION,CHECKED,GUIDANCE,OVERVIEW,extend
from content import skill
from revision import pack
extend(K,R,skill,pack)
ROOT=Path(__file__).resolve().parents[1]
subject='Maths' if ROOT.name=='KS3Maths' else 'Science'
site='ks3-'+subject.lower()
units=[];lessons=[];numbers={7:0,8:0,9:0};legacy={};term_numbers={}
for year,title,keys in UNITS:
 numbers[year]+=1;uid=f'y{year}-unit-{numbers[year]:02}'
 legacy[uid]=dict(year=year,title=title,skills=keys.split())
planned={p[2] for p in PLAN}
ordered=[]
for year in [7,8,9]:
 ordered += [p for p in PLAN if p[0]==year]
 ordered += [(year,'Extra revision',uid,u['title'],' '.join(u['skills']),' '.join(u['skills'])) for uid,u in legacy.items() if u['year']==year and uid not in planned]
numbers={7:0,8:0,9:0}
for year,term,uid,title,keys,challenge in ordered:
 numbers[year]+=1;term_numbers[(year,term)]=term_numbers.get((year,term),0)+1
 old=legacy.get(uid);skills=list(dict.fromkeys(keys.split()+(old['skills'] if old else [])))
 extra=uid not in planned;index=next((i for i,p in enumerate(PLAN) if p[2]==uid),None)
 units.append(dict(id=uid,year=year,number=numbers[year],title=title,skills=skills,term=term,block=term_numbers[(year,term)],optional=uid in OPTIONAL,extra=extra,extend_skills=challenge.split(),review_skills=old['skills'] if old else skills,source_page=74+index if index is not None else None))
 for n,key in enumerate(skills,1):
  l=copy.deepcopy(K[key]);l.update(id=uid+'-'+key,unit=uid,year=year,number=n)
  l['extension']=extra or key in challenge.split();l['optional']=uid in OPTIONAL;l['term']=term
  l['marks']=len(l['scheme'])
  revision=copy.deepcopy(R[key]);shift=int(hashlib.sha256(l['id'].encode()).hexdigest()[:8],16)%3
  quiz=revision['quiz'];quiz['opts']=quiz['opts'][shift:]+quiz['opts'][:shift];quiz['a']=(-shift)%3
  l['cards']=revision['cards'];l['quiz']=quiz
  l['misconception']=dict(q=R[key]['quiz']['q']+' Sam answers: “'+R[key]['quiz']['opts'][1]+'” Explain why this is wrong.',m=2,ms=[R[key]['quiz']['opts'][0],R[key]['quiz']['why']])
  if 'review' in revision:l['review']=revision['review']
  lessons.append(l)
papers=[]
for (year,letter),questions in P.items():
 paper=dict(id=f'y{year}-paper-{letter.lower()}',year=year,paper=letter,title=f'Year {year} · Version 3 review' if letter=='C' else f'Year {year} · Practice paper {letter}',basis='Version 3 route' if letter=='C' else 'Department revision',minutes=35,marks=sum(q['m'] for q in questions),coverage=COVERAGE[year] if letter=='C' else [u['title'] for u in legacy.values() if u['year']==year],questions=[dict(title=q['title'],stem='',parts=[q]) for q in questions])
 papers.append(paper)
sources=[dict(title='Department 2026–27 teaching sequence',kind='curriculum',detail='Adapted from the lesson folders and planning workbooks supplied by the department. Revision pages consolidate related teaching periods; original slides, staff allocations and school tests are not reproduced.'),dict(title='National curriculum: '+subject.lower(),url='https://www.gov.uk/government/publications/national-curriculum-in-england-'+('mathematics' if subject=='Maths' else 'science')+'-programmes-of-study')]
sources.insert(0,dict(title='White Rose Maths Version 3 · 2026 curriculum guidance',url=GUIDANCE,kind='curriculum',detail='Main Year 7–9 blocks follow the Version 3 sequence. Prodigy explanations, questions and drawings are original. Department extension pages remain available separately.'))
sources.insert(1,dict(title='White Rose secondary yearly overviews',url=OVERVIEW))
if subject=='Science':sources += [dict(title='NHS: young people and vaping',url='https://www.nhs.uk/better-health/quit-smoking/help-others-quit/young-people-and-vaping/'),dict(title='Met Office: causes of climate change',url='https://weather.metoffice.gov.uk/climate-change/causes-of-climate-change')]
assert set(K)==set(R), 'Each Maths concept needs word cards and a checked retrieval question.'
alignment=dict(scheme=VERSION,checked=CHECKED,guidance=GUIDANCE,overview=OVERVIEW,document_year=2026,main_blocks=len(PLAN),optional_blocks=len(OPTIONAL),extra_blocks=sum(u['extra'] for u in units),scope='Block sequence and topic coverage, with original revision lessons and representation types. This is an independent revision companion, not a reproduction of every White Rose small-step resource or an endorsed White Rose product.')
course=dict(title='KS3 '+subject,site=site,reviewed=CHECKED,alignment=alignment,units=units,lessons=lessons,sources=sources)
(ROOT/'course.json').write_text(json.dumps(course,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'paper-bank.json').write_text(json.dumps(papers,ensure_ascii=False,indent=2),encoding='utf-8')
(ROOT/'course-data.js').write_text('window.KS_COURSE='+json.dumps(course,ensure_ascii=False)+';\nwindow.KS_PAPERS='+json.dumps(papers,ensure_ascii=False)+';\n',encoding='utf-8')
(ROOT/'coverage.json').write_text(json.dumps(dict(course=course['title'],reviewed=course['reviewed'],alignment=alignment,learning=dict(format='Short swipeable slides, labelled diagrams, worked steps, word cards and practice',lessons=len(lessons),concepts=len(K),questions_per_lesson=4,unit_checks=len(units),definition_cards=sum(len(l['cards']) for l in lessons)),years=[dict(year=y,units=[dict(id=u['id'],title=u['title'],term=u['term'],block=u['block'],optional=u['optional'],extra=u['extra'],guidance_page=u['source_page'],lessons=[dict(id=l['id'],title=l['title'],extra_challenge=l['extension']) for l in lessons if l['unit']==u['id']]) for u in units if u['year']==y]) for y in [7,8,9]],papers=[dict(id=p['id'],title=p['title'],basis=p['basis'],coverage=p['coverage']) for p in papers],note='The main route follows White Rose secondary Version 3 (2026 guidance); additional department revision is labelled separately. Lessons consolidate related small steps. Three original route reviews sample the revised yearly topics; six previous department papers are retained. Unit checks cover the expanded route.'),ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(site=site,units=len(units),lessons=len(lessons),papers=len(papers),marks=[p['marks'] for p in papers])))
