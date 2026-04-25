import os

data = {
  'Zurich': '# Zurich\n\n**音标**: /ˈzʊərɪk/\n\n**词性**: n.\n\n**释义**: 苏黎世（瑞士最大城市，商业和文化中心）\n\n**例句** (原文): In the spring of 1916 in Zurich, young people gathered on a small stage in a bar...',
  'cardboard': '# cardboard\n\n**音标**: /ˈkɑːrdbɔːrd/\n\n**词性**: n.\n\n**释义**: 硬纸板，纸板（常用于制作盒子或简易服装等）\n\n**例句** (原文): ...sometimes dressed in cardboard, often performing nonsense poems.',
  'Dada': '# Dada\n\n**音标**: /ˈdɑːdɑː/\n\n**词性**: n.\n\n**释义**: 达达主义（第一次世界大战期间产生于瑞士苏黎世的一场反传统的艺术与文学运动）\n\n**例句** (原文): This was the start of Dada, a cultural phenomenon that spread to other cities in war-torn Europe...',
  'inevitability': '# inevitability\n\n**音标**: /ɪnˌevɪtəˈbɪləti/\n\n**词性**: n.\n\n**释义**: 必然性，不可避免（指必然发生，无法逃避的状况）\n\n**例句** (原文): ...part protest against the inevitability of constant wars on the continent, part artistic experiment.',
  'since what': '# since what\n\n**音标**: /sɪns hwʌt/\n\n**词性**: phrase\n\n**释义**: 既然什么（在句中表示无奈或反诘：既然这样，到底还有什么是有意义的）\n\n**例句** (原文): And if the poem, songs, costumes and art made no sense, well, that was deliberate, since what, after all, could make sense to people of conscription age...',
  'conscription': '# conscription\n\n**音标**: /kənˈskrɪpʃn/\n\n**词性**: n.\n\n**释义**: 征兵，义务兵役（尤指战时的强制入伍）\n\n**例句** (原文): ...since what, after all, could make sense to people of conscription age, horrified by the killing?',
  'horrified': '# horrified\n\n**音标**: /ˈhɔːrɪfaɪd/\n\n**词性**: adj.\n\n**释义**: 惊骇的，充满恐惧的（表示极其震惊和反感）\n\n**例句** (原文): ...since what, after all, could make sense to people of conscription age, horrified by the killing?',
  'Emeritus': '# Emeritus\n\n**音标**: /iˈmerɪtəs/\n\n**词性**: adj.\n\n**释义**: 荣誉退休的，名誉的（多指大学教授退休后保留头衔）\n\n**例句** (原文): With me to discuss Dadaism are Dawn Addis, Emeritus Professor of Art History and Theory at the University of Essex...',
  'mechanised': '# mechanised\n\n**音标**: /ˈmekənaɪzd/\n\n**词性**: adj.\n\n**释义**: 机械化的（配备机器或机械武器的，特别是战争或工业中）\n\n**例句** (原文): So 1915-16, we are, of course, in the middle of World War I, the mechanised mass murder of the Western Front.',
  'Western Front': '# Western Front\n\n**音标**: /ˈwɛstərn frʌnt/\n\n**词性**: n.\n\n**释义**: 西线（一战中的主要战区，位于欧洲西部）\n\n**例句** (原文): So 1915-16, we are, of course, in the middle of World War I, the mechanised mass murder of the Western Front.',
  'Balkans': '# Balkans\n\n**音标**: /ˈbɔːlkənz/\n\n**词性**: n.\n\n**释义**: 巴尔干半岛（欧洲东南部地区）\n\n**例句** (原文): The war, of course, extends across Central Europe into the Balkans.',
  'Rampant': '# Rampant\n\n**音标**: /ˈræmpənt/\n\n**词性**: adj.\n\n**释义**: 猖獗的，泛滥的（形容不良事物不受控制地蔓延）\n\n**例句** (原文): Rampant nationalism is on the rise.',
  'Ottoman Empire': '# Ottoman Empire\n\n**音标**: /ˈɒtəmən ˈɛmpaɪər/\n\n**词性**: n.\n\n**释义**: 奥斯曼帝国\n\n**例句** (原文): The Ottoman Empire is collapsing.',
  'aspiring': '# aspiring\n\n**音标**: /əˈspaɪərɪŋ/\n\n**词性**: adj.\n\n**释义**: 有抱负的，有志向的（希望成就某事或成为某行业的成功人士）\n\n**例句** (原文): So if you\'re an aspiring student or an aspiring writer or artist...',
  'brutally': '# brutally\n\n**音标**: /ˈbruːtəli/\n\n**词性**: adv.\n\n**释义**: 残忍地，野蛮地\n\n**例句** (原文): ...and you don\'t want to be brutally murdered in an insane war or in social unrest...',
  'unrest': '# unrest\n\n**音标**: /ʌnˈrɛst/\n\n**词性**: n.\n\n**释义**: 动荡，骚动（尤指社会的动乱状态）\n\n**例句** (原文): ...and you don\'t want to be brutally murdered in an insane war or in social unrest, then Zurich is a pretty good bet.',
  'Switzerland': '# Switzerland\n\n**音标**: /ˈswɪtsərlənd/\n\n**词性**: n.\n\n**释义**: 瑞士\n\n**例句** (原文): Switzerland, of course, is neutral.',
  'ferociously': '# ferociously\n\n**音标**: /fəˈroʊʃəsli/\n\n**词性**: adv.\n\n**释义**: 极其，猛烈地（形容程度非常深）\n\n**例句** (原文): It\'s German-speaking but ferociously multilingual, multicultural.',
  'refuge': '# refuge\n\n**音标**: /ˈrɛfjuːdʒ/\n\n**词性**: n.\n\n**释义**: 避难所，庇护所（提供安全的地点）\n\n**例句** (原文): It\'s a site where people are seeking refuge.',
  'proto-Dadaists': '# proto-Dadaists\n\n**音标**: /ˈproʊtoʊ-ˈdɑːdɑːɪsts/\n\n**词性**: n.\n\n**释义**: 早期达达主义者，原始达达主义者（指在达达运动正式确立之前就有类似思想倾向的人）\n\n**例句** (原文): It has a university where a lot of our Dadaists and proto-Dadaists are enrolled.',
  'enrolled': '# enrolled\n\n**音标**: /ɪnˈroʊld/\n\n**词性**: adj./v. (过去分词作表语)\n\n**释义**: 注册，加入（学校、课程等）\n\n**例句** (原文): It has a university where a lot of our Dadaists and proto-Dadaists are enrolled.',
  'heavyweight': '# heavyweight\n\n**音标**: /ˈhɛviweɪt/\n\n**词性**: n.\n\n**释义**: 重量级人物，重要人物（在某个领域中有影响力和地位的人）\n\n**例句** (原文): And, of course, Zurich is home at that time to a lot of cultural and political heavyweights.',
  'Lenin': '# Lenin\n\n**音标**: /ˈlɛnɪn/\n\n**词性**: n.\n\n**释义**: 列宁（俄国革命家）\n\n**例句** (原文): Lenin is there with Nadezhda Kripskaya as well.',
  'Nadezhda Kripskaya': '# Nadezhda Kripskaya\n\n**音标**: /nəˈdɛʒdə krɪpˈskaɪə/\n\n**词性**: n.\n\n**释义**: 娜杰日达·克鲁普斯卡娅（列宁的妻子）\n\n**例句** (原文): Lenin is there with Nadezhda Kripskaya as well.',
  'Anglo-centric': '# Anglo-centric\n\n**音标**: /ˌæŋɡloʊˈsɛntrɪk/\n\n**词性**: adj.\n\n**释义**: 以英美为中心的，盎格鲁中心的\n\n**例句** (原文): But it\'s in some ways a sort of an unlikely place looking, I guess, back at it from a kind of, you know, a kind of Anglo-centric perspective.',
  'immediate context': '# immediate context\n\n**音标**: /ɪˈmiːdiət ˈkɒntɛkst/\n\n**词性**: n. phrase\n\n**释义**: 直接背景，当时的直接环境\n\n**例句** (原文): But if you think about the immediate context, it makes a lot of sense as a place where people can go...',
  'energized': '# energized\n\n**音标**: /ˈɛnərdʒaɪzd/\n\n**词性**: adj.\n\n**释义**: 充满活力的，被激发的\n\n**例句** (原文): ...be safe, but also be energized and come together around this feeling.',
  'absurd': '# absurd\n\n**音标**: /əbˈsɜːrd/\n\n**词性**: adj./n.\n\n**释义**: 荒谬的，荒唐的；（作为名词）荒谬的事物\n\n**例句** (原文): But can you give us a first taste of the link between Dada and the absurd?',
  'cabaret': '# cabaret\n\n**音标**: /ˈkæbəreɪ/\n\n**词性**: n.\n\n**释义**: 卡巴莱（一种有歌舞、戏剧表演的餐馆或夜总会）\n\n**例句** (原文): ...who, with Emmy Hennings, has already been on the scene as a cabaret sort of empresario.',
  'empresario': '# empresario\n\n**音标**: /ˌɛmprɪˈsɑːrioʊ/\n\n**词性**: n.\n\n**释义**: 娱乐业经纪人，演出经营者（原文拼写可能为 impresario）\n\n**例句** (原文): ...who, with Emmy Hennings, has already been on the scene as a cabaret sort of empresario.',
  'Nietzsche': '# Nietzsche\n\n**音标**: /ˈniːtʃə/\n\n**词性**: n.\n\n**释义**: 尼采（德国哲学家）\n\n**例句** (原文): And Bough was very interested in Nietzsche\'s work on the absurd.',
  'self-satire': '# self-satire\n\n**音标**: /sɛlf-ˈsætaɪər/\n\n**词性**: n.\n\n**释义**: 自我讽刺，自嘲\n\n**例句** (原文): There\'s also a degree of self-satire in the absurd.',
  'Self-idiocy': '# Self-idiocy\n\n**音标**: /sɛlf-ˈɪdiəsi/\n\n**词性**: n.\n\n**释义**: 自我愚蠢，自我白痴化（表现出极度愚蠢以达到艺术或挑衅目的）\n\n**例句** (原文): Self-idiocy is a key theme of Dada.'
}

output_dir = '/Users/pengfei.ma/Library/CloudStorage/OneDrive-UniversityofGlasgow/Documents/GitHub/quartz/content/learning-english/dictionary'
os.makedirs(output_dir, exist_ok=True)

count = 0
for word, content in data.items():
    safe_name = word.replace('/', '-')
    file_path = os.path.join(output_dir, f'{safe_name}.md')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    count += 1
    print(f'Generated: {file_path}')

print(f'Successfully created {count} files in {output_dir}')
