import praw
import config
import random
import time
import prawcore.exceptions

# List of image URLs (excluding .mp4)
images = [
    "https://i.imgur.com/45BQxlW.jpeg",
    "https://i.imgur.com/1VNgKhR.jpeg",
    "https://i.imgur.com/cyb9mRY.png",
    "https://i.imgur.com/oIcymy2.jpeg",
    "https://i.imgur.com/yRwbaU6.jpeg",
    "https://i.imgur.com/dnMMkAz.jpeg",
    "https://i.imgur.com/JeKePjI.png",
    "https://i.imgur.com/tYSiGMv.jpeg",
    "https://i.imgur.com/ueW1Hvm.jpeg",
    "https://i.imgur.com/FliBukq.jpeg",
    "https://i.imgur.com/omBHcpj.jpeg",
    "https://i.imgur.com/ePvK65Q.jpeg",
    "https://i.imgur.com/V09VqZn.jpeg",
    "https://i.imgur.com/0aVIH1u.jpeg",
    "https://i.imgur.com/Dbtieqm.jpeg",
    "https://i.imgur.com/ZYaJspM.png",
    "https://i.imgur.com/5Z8S8Uz.jpeg"
]

# List of phrases
phrases = [
    "Did someone say my name! [That's me]({image})",
    "Woof! Who's talking about me? [Here I am]({image})",
    "Hey there! Someone mentioned Mr. Peanutbutter? [That's me]({image})",
    "You called? Mr. Peanutbutter at your service! [Check this out]({image})",
    "What's up? Did I hear my name? [Here I am]({image})",
    "You rang? Mr. Peanutbutter is here! [Take a look]({image})",
    "Hey, it's me! Mr. Peanutbutter! [That's right]({image})",
    "Did somebody mention me? [Here I am]({image})",
    "Mr. Peanutbutter reporting for duty! [See me here]({image})",
    "Who’s a good dog? It’s me, Mr. Peanutbutter! [Look at this]({image})",
    "Heard my name! Mr. Peanutbutter here! [See this]({image})",
    "Hello there! Did someone say Mr. Peanutbutter? [That's me]({image})",
    "What's happening? Mr. Peanutbutter is on the case! [Check it out]({image})",
    "Here I am! Mr. Peanutbutter, ready and wagging! [See me]({image})",
    "Did I hear my name? Woof! [Here I am]({image})"
]

erica_phrases = [
    "Oh Erica... she’s had quite the journey. Remember when she lost a foot but gained a new tooth?",
    "Erica's been through a lot. She once had a split-brain procedure, but she's still got one good eye to see the world!",
    "Erica had to spend time in the burn ward, but she came out stronger and with a new tooth!",
    "Erica might have only one foot, but she's got a big heart and a new tooth to smile with!",
    "Erica's been through many changes, including a split-brain procedure. At least she still has the right number of ears now!",
    "Erica can’t be around kids for legal reasons, but she’s got one good eye to keep an eye on us all!",
    "She can’t vote in national elections, but Erica’s still a star with her one good eye and her remarkable resilience.",
    "Erica's life hasn’t been easy, with all the changes she’s gone through. From losing a foot to gaining a new tooth, she’s truly amazing!",
    "Erica might have had a split-brain procedure and can't be around children, but she’s got a strong spirit and a good eye for the important things.",
    "Erica might have only one foot, but she’s got plenty of courage and a new tooth to show off!",
    "Erica’s story is unique—losing a foot and gaining a friend along the way. She’s got one good eye on the prize!",
    "Mentioned Erica? She’s come a long way from her time in the burn ward, and she’s still got a great sense of humor!",
    "Heard Erica’s name? She might have had a split-brain procedure, but she’s still as vibrant and resilient as ever!",
    "Erica! What are you doing here with a child-sized coffin?",
    "Erica, you can't be here! this place is filled with childeren..",
    "Did I ever tell ya about my buddy Erica, Third Degree Burns over 95% percent of her body."
]

def login():
    print("Logging in...")
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_id=config.client_id,
                    client_secret=config.client_secret,
                    user_agent='windows:mr_peanutbutter_bot:v1.0 (by /u/Ocean-Thunder)')
    print("Logged in")
    return r

def shoo_dog(r):
    while True:
        attempt = 1
        max_attempts = 5
        while attempt <= max_attempts:
            print(f"Attempt {attempt}: Obtaining comments")
            try:
                for comment in r.subreddit('BoJackHorseman').comments(limit=100):
                    if "erica" in comment.body.lower() and not comment.saved and comment.author.name != config.username:
                        print('Erica mentioned!')
                        erica = random.choice(erica_phrases)
                        comment.reply(erica)
                        comment.save()
                        print(f'Replied to comment {comment.id} by {comment.author.name} with phrase: {erica}')
                        time.sleep(60)
                    
                    elif "who's that dog" in comment.body.lower() and not comment.saved and comment.author.name != config.username:
                        print("Who's that dog?")
                        comment.reply(f'''Mr. Peanutbutter's house\n
                        Who's that dog? Mr. Peanutbutter! (Knick knack, paddywhack, give a dog a bone)\n
                        Who's that dog? Mr. Peanutbutter! (Trying to catch a break, Jack, leave a dog alone)\n
                        He's a dirty dog, he's just trying to do his job\n
                        Who's that dog? Mr. Peanutbutter! (Knick knack, paddywhack, give a dog a bone)\n
                        [listen?](https://www.youtube.com/watch?v=uZQ7pDFZ_-8)''')
                        print(f"Replied to comment {comment.id} by {comment.author.name} with Mr. Peanutbutter's theme")
                        comment.save()
                        time.sleep(60)
                    elif 'mr. peanutbutter' in comment.body.lower() and not comment.saved and comment.author.name != config.username:
                        print('Found one!')
                        image_url = random.choice(images)
                        phrase = random.choice(phrases).format(image=image_url)
                        comment.reply(phrase)
                        print(f'Replied to comment {comment.id} by {comment.author.name} with phrase: {phrase}')
                        comment.save()
                        time.sleep(60)  # Sleep to avoid rapid requests

                # Successfully obtained comments, so exit the retry loop
                break

            except praw.exceptions.APIException as e:
                print(f"API error occurred: {e}")
                if e.error_type == 'RATELIMIT':
                    print(f'Rate limit exceeded. Retrying in {e.retry_after} seconds.')
                    time.sleep(e.retry_after)
                else:
                    time.sleep(60)
                break  # Break retry loop to prevent infinite retries

            except praw.exceptions.ClientException as e:
                print(f'Client error occurred: {e}')
                time.sleep(60)
                break

            except prawcore.exceptions.RequestException as e:
                print(f"Request error occurred: {e}")
                time.sleep(60)
                break

            except prawcore.exceptions.OAuthException as e:
                print(f"OAuth error occurred: {e}")
                print("Check your OAuth credentials and try again.")
                return  # Exit the script if OAuth credentials are incorrect

            except Exception as e:
                print(f'An unexpected error occurred: {e}')
                delay = 2 ** (attempt - 1)  # Exponential backoff calculation
                print(f'Retrying in {delay} seconds...')
                time.sleep(delay)
                attempt += 1
                if attempt > max_attempts:
                    print("Max attempts reached. Exiting this attempt.")
                    break  # Exit retry loop after max attempts

        # Delay before starting the next round of comments
        print("Waiting before the next round...")
        time.sleep(300)  # Sleep for 5 minutes before starting the next round

if __name__ == "__main__":
    r = login()
    shoo_dog(r)
