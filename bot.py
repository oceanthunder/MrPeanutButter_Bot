import praw
import config
import random
import time

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
                for comment in r.subreddit('BojackHorseman').comments(limit=100):
                    if 'Mr. Peanutbutter' in comment.body and not comment.saved and comment.author.name != config.username:
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

            except praw.exceptions.RequestException as e:
                print(f"Request error occurred: {e}")
                time.sleep(60)
                break

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
