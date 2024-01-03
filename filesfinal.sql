ALTER USER 'root'@'localhost' IDENTIFIED WITH 'caching_sha2_password' BY 'sanya1213';
create table topics(id int,
topic_number int,
subject varchar(50),
topic_name varchar(50),
grade varchar(50),
pdf_path blob);

insert into topics values(111, 1,'Maths','Number Operations','Primary School',"MathsLevel1NumberOperations.pdf");
insert into topics values(112, 2, 'Maths','Time','Primary School',"MathsLevel1Time.pdf");
insert into topics values(113, 3,'Maths','Geometry','Primary School',"MathsLevel1Geometry.pdf");
insert into topics values(121, 1,'Maths','Algebra','Middle School',"MathsLevel2Algebra.pdf");
insert into topics values(122, 2,'Maths','Decimals and Fractions','Middle School',"MathsLevel2DecimalsFractions.pdf");
insert into topics values(123,3,'Maths','Ratios and Proportions','Middle School',"MathsLevel2Ratios.pdf");
insert into topics values(131,1,'Maths','Calculus','High School',"MathsLevel3Calculus.pdf");
insert into topics values(132,2,'Maths','Probability and Statistics','High School',"MathsLevel3ProbStats.pdf");
insert into topics values(211,1,'English','Adjectives and Adverbs','Primary School',"EnglishLevel1AdjectivesAdverbs.pdf");
insert into topics values(212,2,'English','Nouns and Pronouns','Primary School',"EnglishLevel1NounsPronouns.pdf");
insert into topics values(213,3,'English','Verbs','Primary School',"EnglishLevel1Verbs.pdf");
insert into topics values(221,1,'English','Active and Passive Voice','Middle School',"EnglishLevel2ActivePassive.pdf");
insert into topics values(222,2,'English','Punctuation and Sentence Structure','Middle School',"EnglishLevel2PuncandSentences.pdf");
insert into topics values(231,1,'English','Figures of Speech','High School',"EnglishLevel3FigsofSpeech.pdf");
insert into topics values(232,2,'English','Advanced Grammar','High School',"EnglishLevel3AdvancedGrammar.pdf");
