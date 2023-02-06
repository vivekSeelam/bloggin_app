# bloggin_app
This is a blogging app using python Django -- well not really

This is a playground project I made which started off wanting me to learn Django and build a bloggin app.
But then I saw everybody talk about chatGPT and it is so cool!

Then I got this idea

So the idea is to build some software which automatically writes blog for you and earns you some money.

But what will you write about?
Obviously something that people are talking/searching about.
This brought me to use the pytrends API which accepts the location as an argument and then returns the top trending topics people are searching for.

Then I use them to ask ChatGPT to generate some blogging topics.

Then I pass those blogging topics to ChatGPT to write a blog on that topic.

I could create my own bloggin app, but I am trying to use wordpress to publish those blogs. I am using selenium to automatically open my account and paste stuff and publish. (This seems a bit flaky I am sure there must be a better way, but I will go with this temporarily)
