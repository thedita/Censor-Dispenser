# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# I need to add explanations everywhere
# Now, I want to censor a word or phrase from the email. I also want to preserve the length of the word or phrase
def replace(word):
  return '*' * len(word)

def make_comprehensive(lst):
  new_lst = lst
  for i in lst:
    if not(i.upper() in new_lst):
      new_lst.append(i.upper())
    if not(i.lower() in new_lst):
      new_lst.append(i.lower())
    if not(i.title() in new_lst):
      new_lst.append(i.title())
  return new_lst
def censor_a_list(text, censor_list):
  to_censor = make_comprehensive(censor_list)
  for censor in to_censor:
    if censor in text:
      text = text.replace(censor, replace(censor))
  return text

def make_positive(text, censor_list, negative_list):
  text2 = censor_a_list(text, censor_list) # censor it first
  comprehensive_neg_list = make_comprehensive(negative_list)
  location_list = [] 
  for i in range(len(comprehensive_neg_list)):
    location_list.append(text2.find(comprehensive_neg_list[i]))
  min_num = len(text2)
  index = 0
  for i in range(len(comprehensive_neg_list)):
    if location_list[i] != -1 and location_list[i] < min_num:
      min_num = location_list[i]
      index = i
  word_len = len(comprehensive_neg_list[index])
  split1 = text2[:(min_num + word_len)]
  split2 = text2[(min_num + word_len):]
  censored_split = censor_a_list(split2, comprehensive_neg_list) # posify the rest
  return(split1 + censored_split)

# this needs to be abstracted
def censor_surrounding(text):
  paragraphs = text.split('\n')
  new_paragraphs = []
  for paragraph in paragraphs:
    words = paragraph.split()
    new_words = []
    if len(words) <= 1:
      new_paragraphs.append(paragraph)
    else:
      for i in range(len(words)):
        if i == 0 and '*' in words[1]:
          new_words.append(replace(words[i]))
        elif i == 0:
          new_words.append(words[i])
        elif i == len(words) - 1 and '*' in words[-2]:
          new_words.append(replace(words[i]))
        elif i == len(words) -1:
          new_words.append(words[i])
        elif '*' in words[i + 1] or '*' in words[i - 1]:
          new_words.append(replace(words[i]))
        else:
          new_words.append(words[i])
    new_paragraphs.append(' '.join(new_words))
  return create_email_txt(new_paragraphs)

def create_email_txt(text):
  return '\n'.join(text)


# Censor Email One
censored_email_one = censor_a_list(email_one, ["learning algorithms"])
#print(censored_email_one)

# Censor Email Two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
censored_email_two = censor_a_list(email_two, proprietary_terms)
#print(censored_email_two)

# Censor Email Three
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing", "concerning", "horrible", "horribly", "questionable"]
example_txt = "This is out of control. I am concerned that this project is horrible, awful, and broken."
#print(make_positive(example_txt, negative_words))

censored_email_three = make_positive(email_three, proprietary_terms, negative_words)

#print(censored_email_three)


# Censor Email Four
censored_email_four = make_positive(email_four, proprietary_terms, negative_words)

completely_censored_email_four = (censor_surrounding(censored_email_four))
print(completely_censored_email_four)

# needs some cleaning up but good for now