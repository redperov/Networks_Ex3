# -*- coding: utf-8 -*-


def get_article(num_of_article):
    switcher = {
        1: ARTICLE1,
        2: ARTICLE2,
        3: ARTICLE3,
        4: ARTICLE4,
        5: ARTICLE5,
        6: ARTICLE6,
        7: ARTICLE7,
        8: ARTICLE8,
    }

    article = switcher.get(num_of_article)

    return article


ARTICLE1 = {
  'link' : 'http://www.ynet.co.il/articles/0,7340,L-4713571,00.html',
  'img' : 'https://images1.ynet.co.il/PicServer4/2014/08/05/5506384/52203970100690640360no.jpg',
  'title' : 'החוש הדומיננטי שיעזור לכם בלימודים',
  'content' : 'החוש הדומיננטי שיעזור לכם￼￼￼ בלימודים. אילו טיפים של שימוש בחושים יעזרו לכם?',
}

ARTICLE2 = {
  'link' : 'http://www.ynet.co.il/articles/0,7340,L-5045541,00.html',
  'img' : 'https://images1.ynet.co.il/PicServer5/2017/11/23/8172884/817287001000100980704no.jpg',
  'title' : '"כ"ט בנובמבר: "שמחה שנמשכה ימים ולילות,￼ הייתה אופוריה"',
  'content' : 'ב-1947 הם היו ילדים או צעירים￼￼￼￼￼￼ בתחילת דרכם, אבל את היום הגורלי ב-29 בנובמבר הם לא\
              שוכחים עד היום. "כולם היו צמודים לרדיו. אני זוכרת את התפרצות השמחה, ריקודים\
              והתחבקויות".',
}

ARTICLE3 = {
  'link' : 'https://www.calcalist.co.il/world/articles/0,7340,L-3726321,00.html',
  'img' : 'https://images1.calcalist.co.il/PicServer3/2017/11/30/775736/2_l.jpg',
  'title' : 'רוצים נייר טואלט? הזדהו: כך משפרים הסינים￼ את מצב השירותים הציבוריים',
  'content' : 'שבוע קרא נשיא סין שי ג‘ינפינג￼￼￼￼￼￼ להמשיך את מהפכת השירותים הציבוריים עליה הכריז ב-2015.ֿֿ\
                עד כה שופצו ונבנו 68 אלף מתקנים',
}

ARTICLE4 = {
  'link' : 'http://www.nrg.co.il/online/13/ART2/902/962.html',
  'img' : 'http://www.nrg.co.il/images/archive/465x349/1/646/416.jpg',
  'title' : 'מחקו לכם הודעה בווטסאפ? עדיין תוכלו לקרוא אותה',
  'content' : 'פליקציה בשם Noti cation History מאפשרת למשתמשי  אנדרואיד לקרוא את הנתונים הזמניים הנשמרים ביומן הפעילות של הסמארטפון, כולל הודעות מחוקות.'
}

ARTICLE5 = {
  'link' : 'http://www.nrg.co.il/online/55/ART2/904/542.html',
  'img' : 'http://www.nrg.co.il/images/archive/465x349/1/795/429.jpg',
  'title' : 'גם בחורף: זה בדיוק הזמן לקפוץ לאילת',
  'content' : 'העיר הדרומית נעימה לנופש גם￼￼￼￼￼ בחודשי החורף. כעת מוצעים מחירים אטרקטיביים במיוחד בחבילות שכוללות מגוון אטרקציות, לינה וטיסות'
}

ARTICLE6 = {
  'link' : 'https://food.walla.co.il/item/3113079',
  'img' : 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/3/2513314-46.jpg',
  'title' : '12 בתי קפה שמתאימים לעבודה עם לפטופ',
  'content' : 'בין אם אתם סטודנטים או￼￼￼ עצמאיים, זה תמיד סיפור למצוא בית קפה נעים וטעים לרבוץ בו. קיבצנו עבורכם 12 מקומות אהובים בדיוק למטרה זו, בארבע הערים הגדולות'
}

ARTICLE7 = {
  'link' : 'https://news.walla.co.il/item/3114145',
  'img' : 'https://img.wcdn.co.il/f_auto,w_700/2/4/9/5/2495334-46.jpg',
  'title' : 'שותק על אזריה, נלחם באהוד ברק: בנט מנסה להיבנות כימין ממלכתי',
  'content' : 'כשרגב נלחמת ברעש בתאטרון￼￼￼ יפו, בנט משנה בשקט את נהלי סל התרבות כך שהחומרים "השמאלנים" ייפלטו. כשהקשת הפוליטית מתרעמת על דיווחי ה"דיל" של טראמפ עם הפלסטינים, בנט שותק עד שהרשות תסרב.'
}

ARTICLE8 = {
  'link' : 'https://news.walla.co.il/item/3114283',
  'img' : 'https://img.wcdn.co.il/f_auto,w_700/2/5/1/4/2514588-46.jpg',
  'title' : 'רצח בכל שלושה ימים: צרפת יוצאת למאבק￼￼ באלימות נגד נשים',
  'content' : 'אחרי ש-126 נשים נרצחו בידי בני￼￼￼ זוגן בשנה שעברה, הציג מקרון צעדים חדשים למלחמה בתופעה. "זאת בושה לצרפת", אמר הנשיא שאחת מהבטחות הבחירות שלו הייתה להשיג שוויון מגדרי.'
}


ARTICLES = [ARTICLE1, ARTICLE2, ARTICLE3, ARTICLE4, ARTICLE5, ARTICLE6, ARTICLE7, ARTICLE8]
