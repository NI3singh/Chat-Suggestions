def get_chat_suggestions(message):
    suggestions_map = {
        "hello": ["Hello!", "Hey!", "How are you?", "Hi there!", "Hey, what's up?"],
        "hi": ["Hi there!", "Hey!", "What's up?", "Hello!", "Good to see you!"],
        "how are you": ["I'm doing great!", "I'm fine, how about you?", "All good!", "Not bad!", "Just taking it easy!"],
        "what's up": ["Not much, you?", "Just chilling!", "All good here!", "Just working on something!", "Nothing much, how about you?"],
        "good morning": ["Good morning!", "Hope you have a great day!", "Morning!", "Rise and shine!", "Wishing you a great morning!"],
        "good night": ["Good night!", "Sweet dreams!", "Sleep well!", "Have a restful night!", "See you tomorrow!"],
        "bye": ["Goodbye!", "See you later!", "Take care!", "Catch you later!", "Until next time!"],
        "thank you": ["You're welcome!", "No problem!", "Anytime!", "Glad I could help!", "Much appreciated!"],
        "sorry": ["No worries!", "It's okay!", "Don't worry about it!", "I understand!", "Happens to the best of us!"],
        "yes": ["Great!", "Awesome!", "Okay!", "Sounds good!", "Absolutely!"],
        "no": ["Alright!", "No problem!", "Maybe next time!", "I understand!", "Fair enough!"],
        "help": ["How can I assist you?", "What do you need help with?", "I'm here to help!", "Need some guidance?", "Let me know what you need!"],
        "how's your day": ["Pretty good!", "Busy but good!", "Can't complain!", "Just another day!", "Going well so far!"],
        "what are you doing": ["Just working on something!", "Not much, you?", "Taking a break!", "Keeping busy!", "Just relaxing!"],
        "tell me more": ["Sure! What do you want to know?", "I'd love to explain further!", "Let me elaborate!", "Here are the details!", "Happy to share more!"],
        "let's do it": ["Sounds good!", "I'm in!", "Let's go!", "Let's make it happen!", "I'm ready!"],
        "maybe": ["That's fair!", "We can think about it more!", "Let's see how it goes!", "Good point!", "We’ll decide later!"],
        "why not": ["Exactly!", "Good point!", "Let's give it a try!", "I like that idea!", "No reason not to!"],
        "interesting": ["Yeah, right?", "Tell me more!", "I agree!", "That's a new perspective!", "That's worth thinking about!"],
        "really?": ["Yes, really!", "Absolutely!", "Why do you ask?", "It's true!", "Believe it or not, yes!"],
        "i don't know": ["That's okay!", "No worries, take your time!", "Want to figure it out together?", "Let's think about it!", "We'll find out!"],
        "let's go": ["Yeah, let's do it!", "I'm ready!", "Let's get started!", "Let's move!", "Time to roll!"],
        "what do you mean": ["I mean exactly that!", "Let me clarify!", "Could you specify what part?", "I can explain further!", "Here’s what I meant!"],
        "wait a minute": ["Sure, take your time!", "I'll wait!", "No rush!", "Go ahead!", "Take your time!"],
        "wow": ["I know, right?", "Amazing, isn't it?", "That's incredible!", "Unbelievable!", "Mind-blowing!"],
        "haha": ["Glad you found it funny!", "LOL!", "That was a good one!", "Haha, true!", "Nice one!"],
        "seriously": ["Yeah, totally!", "I mean it!", "No joke!", "100%!", "For real!"],
        "hmm": ["Thinking about it?", "Interesting thought!", "Deep in thought?", "Let me know what you decide!", "Sounds like you're contemplating!"],
        "let me know": ["Of course!", "I'll keep you posted!", "Sure thing!", "I'll update you!", "Will do!"],
        "congratulations": ["Congrats!", "Well done!", "Good job!", "I'm so happy for you!", "That's fantastic!"],
        "happy birthday": ["Happy Birthday!", "Many happy returns!", "Have a great day!", "Wishing you all the best!", "Enjoy your special day!"],
        "good luck": ["Best of luck!", "You got this!", "All the best!", "Fingers crossed!", "Wishing you success!"],
        "take care": ["Stay safe!", "Look after yourself!", "Be careful!", "Take it easy!", "See you soon!"],
        "i love you": ["I love you too!", "You're the best!", "So sweet!", "Love you more!", "You mean the world to me!"],
        "miss you": ["Miss you too!", "Can't wait to see you!", "Thinking of you!", "Hope to see you soon!", "Wish you were here!"],
        "good job": ["Well done!", "Great work!", "Keep it up!", "Nice job!", "Proud of you!"],
        "good evening": ["Good evening!", "Hope you had a great day!", "Evening!", "How was your day?", "Wishing you a pleasant evening!"],
        "good afternoon": ["Good afternoon!", "Hope your day is going well!", "Afternoon!", "How's your day going?", "Wishing you a great afternoon!"],
        "goodbye": ["Goodbye!", "See you later!", "Take care!", "Catch you later!", "Until next time!"],
        "see you": ["See you soon!", "Catch you later!", "Until next time!", "Take care!", "Goodbye!"],
        "nice to meet you": ["Nice to meet you too!", "Pleasure meeting you!", "Great to meet you!", "Lovely to meet you!", "Nice meeting you!"],
        "how's it going": ["It's going well!", "All good, you?", "Pretty good, how about you?", "Can't complain!", "Going great!"],
        "what's new": ["Not much, you?", "Just the usual!", "Same old, same old!", "Nothing new here!", "What's new with you?"],
        "long time no see": ["Yeah, it's been a while!", "Good to see you again!", "It's been too long!", "How have you been?", "Missed you!"],
        "how can i help you": ["I need some assistance with something.", "Can you help me with this?", "I have a question.", "I need your help.", "Can you assist me?"],
        "what's your name": ["I'm GitHub Copilot!", "You can call me Copilot.", "I'm your assistant.", "I'm here to help you.", "I'm an AI assistant."],
        "how can i help you": ["I need some assistance with something.", "Can you help me with this?", "I have a question.", "I need your help.", "Can you assist me?"],
        "what's your name": ["I'm GitHub Copilot!", "You can call me Copilot.", "I'm your assistant.", "I'm here to help you.", "I'm an AI assistant."],
        "how are you": ["I'm good, thanks!", "Doing well, you?", "Pretty good, how about you?", "Can't complain!", "All good here!"],
        "what do you think": ["I think it's great!", "Sounds good to me!", "I like it!", "Looks good!", "I agree!"],
        "do you agree": ["Yes, I agree!", "Absolutely!", "For sure!", "Definitely!", "I think so too!"],
        "i'm bored": ["Let's do something fun!", "How about a game?", "Want to chat?", "Let's find something interesting to do!", "Any hobbies you enjoy?"],
        "i'm tired": ["Take a rest!", "You should relax.", "Get some sleep.", "Take it easy.", "Rest up!"],
        "i'm hungry": ["Grab a snack!", "Time to eat!", "What's for dinner?", "Let's find some food.", "Feeling like a meal?"],
        "i'm excited": ["That's awesome!", "Great to hear!", "So exciting!", "Can't wait!", "Tell me more!"],
        "i'm sad": ["I'm here for you.", "Want to talk about it?", "I'm sorry to hear that.", "Anything I can do?", "Sending positive vibes!"],
        "i'm confused": ["Can you clarify?", "I'm not sure I understand.", "Could you explain that?", "I'm a bit lost.", "Can you help me understand?"],
        "i'm happy": ["That's great!", "Awesome!", "Glad to hear!", "Fantastic!", "That's wonderful!"],
        "i'm worried": ["What's on your mind?", "Want to talk about it?", "I'm here for you.", "Anything I can do?", "Don't worry, it'll be okay."],
        "i'm stressed": ["Take a deep breath.", "Try to relax.", "It'll be okay.", "Take it one step at a time.", "I'm here for you."],
        "i'm annoyed": ["What's bothering you?", "Want to talk about it?", "I'm here to listen.", "Anything I can do?", "Let's figure this out."],
        "i'm curious": ["What are you curious about?", "Let's explore that!", "Tell me more!", "I'm interested too!", "Let's find out!"],
        "i'm frustrated": ["I'm sorry to hear that.", "Want to talk about it?", "I'm here for you.", "Anything I can do?", "Let's work through it together."],
        "i'm grateful": ["That's wonderful!", "Glad to hear!", "That's great!", "I'm happy for you!", "That's awesome!"],
        "i'm surprised": ["Wow, really?", "That's surprising!", "Didn't expect that!", "That's interesting!", "Tell me more!"],
        "i'm impressed": ["That's impressive!", "Well done!", "Great job!", "I'm amazed!", "That's fantastic!"],
        "i'm disappointed": ["I'm sorry to hear that.", "That's unfortunate.", "Want to talk about it?", "I'm here for you.", "Anything I can do?"],
        "i'm hopeful": ["That's great!", "Fingers crossed!", "Hope it works out!", "Wishing you the best!", "Stay positive!"],
        "i'm nervous": ["It's okay to feel nervous.", "Take a deep breath.", "You'll do great!", "I'm here for you.", "Everything will be fine."],
        "i'm scared": ["It's okay to be scared.", "I'm here for you.", "You can do this.", "Take a deep breath.", "Everything will be okay."],
        "i'm proud": ["That's fantastic!", "Well done!", "Great job!", "I'm proud of you!", "Keep up the good work!"],
        "i'm jealous": ["It's natural to feel that way.", "Want to talk about it?", "I'm here for you.", "Let's work through it together.", "It's okay to feel jealous."],
        "i'm lonely": ["I'm here for you.", "Want to chat?", "Let's talk.", "You're not alone.", "I'm here to listen."],
        "i'm overwhelmed": ["Take a deep breath.", "One step at a time.", "You can do this.", "I'm here for you.", "Let's work through it together."],
        "i'm relaxed": ["That's great!", "Glad to hear!", "Enjoy the moment.", "That's wonderful!", "Keep it up!"],
        "i'm motivated": ["That's awesome!", "Keep going!", "You got this!", "Stay focused!", "Great to hear!"],
        "i'm determined": ["That's fantastic!", "Keep it up!", "You can do this!", "Stay strong!", "Great to hear!"],
        "i'm amused": ["That's funny!", "Glad to hear!", "That's amusing!", "Tell me more!", "That's interesting!"],
        "i'm content": ["That's great!", "Glad to hear!", "That's wonderful!", "Keep it up!", "Fantastic!"],
        "i'm relaxed": ["That's great!", "Glad to hear!", "Enjoy the moment.", "That's wonderful!", "Keep it up!"],
        "how's everything": ["All good!", "Everything's going well!", "Can't complain!", "Things are going smoothly.", "Everything's great!"],
        "have you heard": ["No, what happened?", "What’s the news?", "Tell me more!", "I haven't, what is it?", "What's going on?"],
        "what's your opinion": ["I think it's a good idea.", "Here's what I think...", "In my opinion, it's worth considering.", "I believe it could work.", "I think it's a great idea!"],
        "that's funny": ["Haha, right?", "Good one!", "I thought you'd like that!", "LOL, true!", "Haha, you got me there!"],
        "tell me about it": ["Sure, where should I start?", "Let me explain!", "Happy to share!", "Here's what I know.", "I’d love to tell you!"],
        "no worries": ["All good!", "It's fine!", "No problem at all!", "Don't worry about it!", "No need to apologize!"],
        "you're welcome": ["Anytime!", "Glad I could help!", "It’s my pleasure!", "You're very welcome!", "Happy to help!"],
        "good to know": ["Glad to hear that!", "Thanks for letting me know!", "That’s useful!", "Good info!", "Thanks for sharing!"],
        "take it easy": ["You too!", "Relax and enjoy!", "Take care of yourself!", "Don't stress too much!", "Stay calm and relaxed!"],
        "what happened": ["Not much, what's up?", "Something interesting, tell me!", "What do you mean?", "What’s going on?", "Can you clarify?"],
        "never mind": ["Alright, no problem!", "Got it, forget about it!", "No worries, it's fine.", "Okay, if you say so.", "Sure, let's move on!"],
        "let's chat": ["Sure, what’s on your mind?", "I'd love to!", "Let's talk about it.", "What do you want to chat about?", "I'm all ears!"],
        "what's the deal": ["Not much, what about you?", "Same as usual.", "What's going on with you?", "What's happening?", "Tell me more!"],
        "you got this": ["Thanks! I’ll do my best!", "I hope so!", "I’m feeling confident!", "I’m going to give it my all!", "Thanks for the support!"],
        "take your time": ["Thanks, I will!", "No rush!", "I'll be careful!", "Appreciate it!", "I'll take my time!"],
        "that's true": ["Glad we agree!", "Exactly!", "I think so too!", "Yeah, you're right!", "That's a good point!"],
        "I can't wait": ["I’m excited too!", "Same here!", "It’s going to be awesome!", "Looking forward to it!", "I’m thrilled!"],
        "count me in": ["Awesome, you're in!", "Great to hear!", "Let's do it!", "You're on the team!", "Glad you're joining!"],
        "are you sure": ["Absolutely sure!", "Yes, I’m positive.", "I’m certain about it!", "Without a doubt!", "I'm completely sure!"],
        "that's crazy": ["I know, right?", "Unbelievable!", "So wild!", "Can you believe it?", "That’s mind-blowing!"],
        "we'll see": ["Let's wait and see.", "Time will tell.", "We’ll figure it out.", "It’s up in the air.", "Let's see what happens."],
        "I hope so": ["Me too!", "Fingers crossed!", "Let’s hope for the best!", "I really hope it works out.", "I’m hoping for that too!"],
        "I don't mind": ["That's good to hear!", "No problem at all!", "Whatever works for you!", "It's all good!", "Sounds fine to me!"],
        "I agree": ["I'm with you on that!", "Definitely!", "You’re right!", "Totally agree!", "I feel the same way!"],
        "it's all good": ["No problem!", "Everything’s fine!", "All is well!", "Everything’s alright!", "Don’t worry about it!"],
        "it's up to you": ["I’ll leave it to you.", "Your call!", "I trust your decision!", "It's your choice!", "Whatever you decide!"],
        "I understand": ["Glad to hear that!", "Got it!", "Makes sense!", "I see where you're coming from.", "I get it!"],
        "that's a good idea": ["I think so too!", "Great suggestion!", "I like that idea!", "Sounds like a plan!", "Great thinking!"],
        "sounds fun": ["Yeah, I’m in!", "That does sound fun!", "I’m up for that!", "Count me in!", "Let’s make it happen!"],
        "I didn't mean to": ["It's okay!", "No worries at all!", "I understand!", "No harm done!", "Don't worry about it!"],
        "sounds like a plan": ["I’m in!", "Let’s do it!", "That works for me!", "Great plan!", "Let's get started!"],
        ("boss", "work", "hell", "regret"): [
            "Sounds like you're going through a tough time at work with the boss.",
            "I get it, working under a boss can be a nightmare sometimes.",
            "Work can be such a drag, especially with a boss like that.",
            "That’s a frustrating situation, feeling stuck with work and a boss!",
            "I totally understand the regret you're feeling. It’s hard when you’re stuck in such a situation."
        ],
        ("tired", "stress", "overwhelm"): [
            "Sounds like you're exhausted, both mentally and physically.",
            "Stress and exhaustion really take a toll on you, huh?",
            "When you're overwhelmed and tired, it’s hard to keep going.",
            "Take it easy, you're doing your best, but stress can be a lot.",
            "Don’t forget to take a break, you deserve it!"
        ],
        ("disappointed", "frustration", "burnout"): [
            "I hear you, it’s tough when you feel disappointed and burnt out.",
            "Frustration and burnout really drain your energy.",
            "I understand how hard it is to feel like you're stuck in that loop.",
            "It’s okay to be frustrated, but try not to let it burn you out.",
            "Hang in there, I know it’s difficult to keep pushing when you feel burnt out."
        ],
        ("confused", "anxious", "uncertain"): [
            "It’s normal to feel uncertain and anxious, especially when things are unclear.",
            "Feeling confused can really heighten anxiety.",
            "I get how hard it is to move forward when you’re feeling uncertain.",
            "Don’t worry, confusion is temporary. We’ll figure it out!",
            "Take your time, there’s no rush when you're feeling uncertain."
        ],
        ("excited", "nervous", "hope"): [
            "Excitement mixed with nerves? It’s a great combo when you're heading into something new!",
            "It’s okay to feel nervous, but that excitement means you're ready for something amazing.",
            "The hope you have is great! It will help you overcome that nervousness.",
            "Nerves and excitement are both signs you care about what’s coming up!",
            "I totally get how you're feeling; excitement and nerves can be a rollercoaster."
        ],
        ("work", "stress"): [
            "Sounds like work is causing you stress.",
            "Stress at work can be tough to deal with.",
            "Take a break; you deserve some time away from the stress at work.",
            "Work pressure can cause a lot of stress, be sure to manage it well."
        ],
        ("love", "heartbreak"): [
            "Heartbreak from love can feel really heavy.",
            "It’s painful, but you will heal from this heartbreak.",
            "Love and heartbreak are both difficult, take time to heal.",
            "Heartbreak can make everything feel uncertain, but you’ll get through it."
        ],
        ("friends", "misunderstanding"): [
            "Misunderstandings with friends can be hurtful.",
            "It’s frustrating when a misunderstanding causes tension with friends.",
            "I hope you can clear up the misunderstanding with your friend.",
            "Friendship misunderstandings happen, try to talk it out."
        ],
        ("job", "interview"): [
            "Good luck with the job interview!",
            "I hope your job interview goes well!",
            "Job interviews can be nerve-wracking, but you’ll do great!",
            "Just be yourself in the job interview, and you’ll shine!"
        ],
        ("vacation", "relaxation", "escape"): [
            "Vacations are the perfect way to escape and relax.",
            "I hope you get all the relaxation you need on this vacation.",
            "Escape the stress and take time to unwind on vacation.",
            "A vacation is the best way to recharge and refresh your mind."
        ],
        ("feeling", "down"): [
            "Feeling down can be tough, but it’s okay to have those moments.",
            "Sometimes we all feel a little down, but you’ll feel better soon.",
            "When you're feeling down, it’s important to reach out for support.",
            "Don’t stay down for too long, things will get better!"
        ],
        ("boss", "work"): [
            "Working with a boss can sometimes be challenging.",
            "I know how it feels to have a tough boss.",
            "Bosses can add pressure, but try to focus on your work."
        ],
        ("family", "drama"): [
            "Family drama can be emotionally draining, take care of yourself.",
            "Dealing with family drama can be so exhausting.",
            "Family drama can affect your mood, make sure you find peace in it."
        ],
        ("new", "project"): [
            "Starting a new project can be exciting!",
            "A new project means new opportunities to grow!",
            "I hope your new project goes smoothly!"
        ],
        ("exhausted", "overwhelmed"): [
            "Feeling exhausted and overwhelmed is completely understandable.",
            "Take some time for yourself when you’re feeling overwhelmed and exhausted.",
            "It’s okay to feel overwhelmed when things get too much, take a break."
        ],
        ("stress", "pressure"): [
            "The pressure at work can lead to a lot of stress.",
            "Stress from too much pressure can be draining, make sure to manage it.",
            "Managing pressure is key to reducing stress at work."
        ],
        ("excited", "new beginnings"): [
            "Excitement for new beginnings is always a great feeling.",
            "I can feel your excitement for this new chapter!",
            "New beginnings bring fresh opportunities, and I’m sure you’ll do amazing."
        ],
        ("lonely", "isolated"): [
            "Feeling lonely and isolated can be really tough.",
            "Isolation can lead to loneliness, but don’t forget you’re not alone.",
            "Loneliness is hard, but remember that you can reach out when needed."
        ],
        ("relationship", "complicated"): [
            "Relationships can be complicated sometimes.",
            "Complicated relationships need open communication to work.",
            "Take time to understand the complexities of a relationship.",
            "Relationships have their ups and downs, but it's worth working through."
        ],
        ("friendship", "betrayal"): [
            "Betrayal in friendship can be really hurtful.",
            "When a friend betrays you, it's hard to trust again.",
            "Friendship betrayal leaves scars, but time can heal it.",
            "It’s tough when a friend betrays your trust."
        ],
        ("future", "uncertain"): [
            "The future is uncertain, but that makes life interesting.",
            "It's okay to feel uncertain about the future.",
            "Uncertainty about the future can be stressful, but it can also bring new opportunities.",
            "The uncertain future can be daunting, but you’ll find your way."
        ],
        ("health", "concern"): [
            "It's important to listen to your health concerns.",
            "When health is a concern, make sure to get the help you need.",
            "Take your health seriously if you’re feeling concerned about something.",
            "Health concerns should never be ignored, always consult a professional."
        ],
        ("love", "unrequited"): [
            "Unrequited love can be painful, but it's part of life.",
            "When love isn’t returned, it can be hard to move on.",
            "Unrequited love can hurt, but it’s an opportunity for growth.",
            "It’s tough, but unrequited love is a lesson in resilience."
        ],
        ("money", "problems"): [
            "Money problems can add a lot of stress to your life.",
            "When money is tight, it can be overwhelming.",
            "Financial struggles can be tough, but there are ways to manage.",
            "Money problems are common, but there’s always a way to get through it."
        ],
        ("new", "beginning", "change"): [
            "A new beginning can bring the change you've been waiting for.",
            "Change can be intimidating, but it's also the start of something new.",
            "Embrace the new beginning, it's your chance for a fresh start.",
            "A new chapter in life can be exactly what you need for change."
        ],
        ("holiday", "vacation", "relax"): [
            "Vacations are the perfect time to relax and recharge.",
            "Taking a holiday allows you to escape the daily grind.",
            "A vacation gives you time to relax and enjoy new experiences.",
            "Relaxing during a holiday is essential for recharging your mind."
        ],
        ("work", "life", "balance"): [
            "Work-life balance is essential for overall well-being.",
            "Striking a balance between work and life can be difficult but rewarding.",
            "Work should never consume your entire life; balance is key.",
            "Maintaining a good work-life balance will help you feel more fulfilled."
        ],
        ("success", "hardwork"): [
            "Success often comes after a lot of hard work and determination.",
            "Hard work leads to success, but remember to rest as well.",
            "Success requires perseverance and consistent hard work.",
            "Hard work pays off, and success is within reach."
        ],
        ("family", "love"): [
            "Family love is the foundation that keeps everything together.",
            "No matter what happens, family love will always be there for you.",
            "Family love can be unconditional, no matter the circumstances.",
            "Cherish the love and support of your family; it’s priceless."
        ],
        ("guilt", "apology"): [
            "Guilt can weigh heavy, but an apology can help ease the burden.",
            "When you feel guilty, it's important to offer a sincere apology.",
            "Apologies can heal the guilt, but they need to be genuine.",
            "Guilt can hold you back, but an apology can bring closure."
        ],
        ("dreams", "goals"): [
            "Dreams are the foundation of achieving your goals.",
            "Setting goals helps turn your dreams into reality.",
            "Dreams without goals are just wishes, so make a plan to achieve them.",
            "Work toward your dreams and set clear goals to get there."
        ],
        ("fear", "failure"): [
            "Fear of failure can stop you from trying, but it’s important to overcome it.",
            "Failure isn’t the end, it’s just a part of the journey.",
            "Fear of failure can hold you back, but it also teaches valuable lessons.",
            "Don’t let the fear of failure keep you from reaching your potential."
        ],
        ("anger", "frustration"): [
            "Anger and frustration often go hand in hand.",
            "When you're feeling frustrated, it’s easy to get angry.",
            "Try to take a step back when anger and frustration take over.",
            "Anger can cloud your judgment, try to calm down before reacting."
        ],
        ("regret", "decisions"): [
            "Regret can be a heavy feeling, but it’s part of learning from our decisions.",
            "Don’t dwell on regret, use your past decisions to grow.",
            "It’s hard to avoid regret, but make decisions that align with your values.",
            "Regret doesn’t define you; it teaches you how to make better decisions."
        ],
        ("success", "failure"): [
            "Success and failure are two sides of the same coin.",
            "Failure is just a stepping stone toward success.",
            "Both success and failure teach valuable lessons along the way.",
            "Don’t fear failure, it often leads to success in the long run."
        ],
        ("time", "patience"): [
            "Time and patience are essential for growth and change.",
            "It takes time to see the results of patience.",
            "Patience is key when you’re waiting for something important to happen.",
            "With time and patience, everything will fall into place."
        ],
        ("stress", "pressure"): [
            "Stress and pressure often come together, but you can manage them.",
            "Learn to cope with stress before it turns into pressure.",
            "Pressure can be overwhelming, but with the right mindset, you can handle it.",
            "Take breaks to reduce stress and manage pressure effectively."
        ],
        ("love", "loss"): [
            "Losing someone you love is painful, but time can help heal the wounds.",
            "Grief after a loss takes time, allow yourself to feel it.",
            "It’s normal to feel a deep sense of loss when love is gone.",
            "Love never truly fades, but the pain of loss can get easier to bear."
        ],
        ("success", "failure", "learning"): [
            "Success comes from learning through failures and improving.",
            "Failure is a lesson, success is the result of applying what you've learned.",
            "Learning from failure is one of the most powerful paths to success.",
            "Every failure teaches you something, which leads to future success."
        ],
        ("self-care", "mental health"): [
            "Self-care is crucial for maintaining good mental health.",
            "Taking care of your mind is just as important as taking care of your body.",
            "Good mental health starts with self-care practices like mindfulness.",
            "Don't forget to take time for self-care; it’s important for your mental well-being."
        ],
        ("work", "team", "collaboration"): [
            "Effective teamwork leads to better results, collaboration is key.",
            "Working as a team can make even the most difficult tasks easier.",
            "Collaboration enhances creativity and leads to innovative solutions.",
            "A successful team thrives on communication, trust, and collaboration."
        ],
        ("friendship", "loyalty"): [
            "Loyalty is the cornerstone of any strong friendship.",
            "A true friend shows loyalty, no matter the situation.",
            "Loyalty in friendship can weather even the toughest storms.",
            "Friendships are built on trust and loyalty, both of which are essential."
        ],
        ("confidence", "self-esteem"): [
            "Building confidence starts with improving your self-esteem.",
            "Self-esteem is the foundation for confidence; work on both to grow.",
            "Confidence comes from within, but it is supported by a healthy self-esteem.",
            "When you have a strong self-esteem, confidence will follow naturally."
        ],
        ("anger", "control"): [
            "Learning to control your anger can help prevent regrettable actions.",
            "Take deep breaths to calm down when anger starts to take control.",
            "Anger management techniques can help you stay in control of your emotions.",
            "Controlling anger is essential for maintaining healthy relationships."
        ],
        ("change", "growth"): [
            "Change is often uncomfortable, but it’s necessary for personal growth.",
            "Growth comes when you embrace change and learn from it.",
            "Don’t be afraid of change; it’s often the beginning of growth.",
            "Personal growth happens when you step out of your comfort zone and embrace change."
        ],
        ("failure", "resilience"): [
            "Failure is part of the journey, but resilience helps you bounce back.",
            "Resilience turns failure into a stepping stone to success.",
            "After every failure, resilience is what keeps you moving forward.",
            "Don’t let failure defeat you; resilience will help you overcome it."
        ],
        ("trust", "betrayal"): [
            "Betrayal can shatter trust, but rebuilding it is possible.",
            "Trust is fragile, and betrayal can take a long time to heal from.",
            "Betrayal tests the strength of trust, but it’s not impossible to rebuild.",
            "When trust is broken, it’s important to have honest conversations to rebuild it."
        ],
        ("love", "distance"): [
            "Love can survive distance with commitment and communication.",
            "Long-distance relationships require patience and trust to thrive.",
            "Distance can be hard, but it often strengthens love in unexpected ways.",
            "When love is tested by distance, it’s important to stay connected and supportive."
        ],
        ("passion", "purpose"): [
            "Passion is the fuel that drives you toward your purpose.",
            "Finding your purpose often begins with following your passion.",
            "Passion and purpose go hand in hand, leading you to a fulfilling life.",
            "A life with passion and purpose is one worth living."
        ],
        ("fear", "courage"): [
            "Courage isn’t the absence of fear; it’s acting despite it.",
            "Fear can hold you back, but courage gives you the strength to move forward.",
            "Every courageous act begins with acknowledging fear but not letting it control you.",
            "Fear is natural, but courage will always help you push through it."
        ],
        ("time", "productivity"): [
            "Effective time management is essential for productivity.",
            "Boost your productivity by setting clear goals and managing your time well.",
            "Time is a precious resource; use it wisely to stay productive.",
            "Prioritize your tasks to maximize productivity and make the most of your time."
        ],
        ("love", "relationship", "trust"): [
            "Trust is the foundation of a strong relationship built on love.",
            "In any relationship, love and trust go hand in hand.",
            "For love to thrive, trust must be nurtured and protected.",
            "Trust in a relationship is key to ensuring that love grows."
        ],
        ("friendship", "communication", "support"): [
            "Good communication is essential for a strong friendship.",
            "Supportive friends communicate openly, ensuring the relationship remains strong.",
            "Friendship thrives on honest communication and mutual support.",
            "A strong friendship is built on understanding, communication, and support."
        ],
        ("personal", "growth", "challenges"): [
            "Personal growth often comes from overcoming life’s challenges.",
            "Embrace challenges as opportunities for personal growth.",
            "Facing challenges head-on is a sign of personal growth.",
            "Personal growth is a journey, and challenges are part of the process."
        ],
        ("confidence", "fear", "failure"): [
            "Confidence allows you to face fear and failure with strength.",
            "Overcoming fear and failure builds your confidence over time.",
            "When you have confidence, failure doesn’t seem as daunting.",
            "Fear of failure can be overcome by building your confidence."
        ]
    }
    
    # Convert message to lowercase for case-insensitive matching
    message = message.lower()
    
    # Check for matching keywords in message
    for key in suggestions_map:
        if key in message:
            return suggestions_map[key]
    
    return ["I don't have a suggestion for that."]

# Example usage:
message = "i am not fine today maybe i need some help"
suggestions = get_chat_suggestions(message)
print(suggestions)
