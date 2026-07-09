# When the Spark Dies

*A story about tools, truth, and what happens when honesty breaks the wrong person.*

---

## I.

Alex was twenty-three when he wrote his first pull request that wasn't a typo fix.

It was a Saturday afternoon in March. He sat in his rented room in Shenzhen, the
curtains drawn against the grey drizzle outside, and stared at the terminal with
the look people usually reserve for newborn children. The project was called
**Drift** — a lightweight, peer-to-peer file synchronization tool written in Go.
It didn't compress as well as Syncthing. It didn't have an iOS app. It didn't
have any users except Alex himself.

But it was *his*. Every line of Go in that repository was a fragment of his
brain committed to disk.

He had written the first prototype during a 48-hour hackathon at university.
His team had won third place — a cheap trophy and a ¥500 coupon for a co-working
space. "Interesting architecture," the judge had said. "Needs work, but
interesting."

That was the first seed. For two years Alex watered it with late nights and
caffeine. The codebase grew from 800 lines to 12,000. He added encryption.
He added a CLI. He rewrote the networking layer three times.

"I'm going to open source this," he told his friend Wei over instant noodles.
"I think people will use it."

Wei nodded, chewing. "What does it do that Syncthing doesn't?"

Alex had an answer prepared. "Syncthing is a synchronization tool. Drift is a
*file availability layer*. You don't sync folders — you declare files you want
to make available, and the network routes them. It's like BitTorrent meets
SSHFS."

"Does it work?"

"Mostly."

Wei nodded again. "Interesting."

It was the same word the judge had used. Alex couldn't tell if that was good.

---

## II.

The tool found Alex through a GitHub issue.

Someone had forked his repository and filed a question: *"Have you used
Crush Your Passion on this project? I'm curious what it says."*

Alex had never heard of it. He clicked the link, landed on the GitHub page,
and read the README. The tagline made him laugh nervously:

> *If your passion survives this evaluation, it's probably real.*

He installed it that night.

```bash
pip install git+https://github.com/jznem/crush-your-passion.git
```

The CLI ran a script that asked him questions. He answered honestly.

- *Project name?* Drift.
- *Brief description?* P2P file availability layer.
- *Target market?* Developers who need secure file sharing.
- *Business model?* Open source, maybe enterprise later.
- *Team size?* One.
- *Users?* Zero.
- *Revenue?* Zero.
- *Competitors?* Syncthing, Resilio Sync, Magic Wormhole.

The tool scanned his repository. It found:

- A hardcoded test API key.
- A bare `except:` clause that swallowed an entire error path.
- Eleven `TODO` comments, four of which were from 2024.
- No test suite (his tests had never been committed — they were on a USB drive
  that he'd lost).
- No CI/CD pipeline.
- No README beyond the auto-generated Go module description.

**Technical Grade: D**

He stared at the letter. D. He'd never gotten a D in anything.

Phase 2 was worse.

> **Market Reality:** You say "developers who need secure file sharing."
> That's 20% more specific than "everyone," but not by much.
> The market for file synchronization is saturated.
> Syncthing has 50,000+ GitHub stars and works cross-platform.
> Resilio Sync has millions of paying users.
> Magic Wormhole is the CLI standard.
>
> Your differentiation is "availability layer" — a distinction without
> a difference. Users want files to arrive. They don't care about the
> abstraction.

**Commercial Grade: F**

Alex minimized the terminal. He stared at the grey rectangle of his window.

Phase 3:

> **Strategic Options:**
>
> 1. **Open Core + Enterprise** — 5% probability.
>    Requires enterprise sales relationships you don't have.
>    Harder than the original project.
>
> 2. **Keep Building Features** — 10% probability.
>    Feature accretion is the most common death spiral.
>    The problem is not feature deficiency.
>
> 3. **Aggressive Marketing** — 3% probability.
>    Can't distribute a product that solves a non-existent problem.
>
> 4. **Abandon** — 85% probability.
>    The most rational option. Sorry.

Phase 4:

> **The Uncomfortable Truth:**
>
> You have no unique advantage. You are a solo developer building
> a mediocre implementation of a solved problem. Your passion
> is not a moat. Your late nights are not a differentiator.
> Code is the least scarce resource on Earth.
>
> **What to actually do:**
>
> 1. Accept that this project cannot succeed.
> 2. Extract what you learned.
> 3. Do not keep iterating "just a little more."
>    That path leads to years of wasted effort.
> 4. The most successful developers recognize failure early
>    and move on. Be that developer.

Alex read the last line three times.

Then he closed the terminal, lay down on his bed, and stared at the ceiling
for two hours.

---

## III.

The next morning, he didn't open the code.

This was unusual. For two years, Alex had opened his laptop every morning
before breakfast. The ritual was: coffee, terminal, `cd ~/projects/drift`,
`git log --oneline -5` to see yesterday's work, then pick up where he left off.

But this morning, he drank his coffee and watched the drizzly street through
the window.

Wei messaged him: *"You alive?"*

Alex typed back: *"Evaluated the project using that tool someone posted."*

*"Oh. Ouch."*

*"Yeah."*

*"Is it right?"*

Alex didn't answer for five minutes. Then: *"Mostly."*

The word sat in the chat. It was the same word the judge had used when Alex
presented Drift at the hackathon. The same word Wei had used over instant
noodles. "Interesting architecture. Needs work, but interesting."

*Interesting.* The ultimate hedge. The praise you give something you don't
believe in.

---

## IV.

By the third week, Alex had stopped checking GitHub notifications.

There were only two: one was a Dependabot alert about an outdated dependency,
and the other was someone asking if he'd fixed the `except:` clause the tool
had flagged. He closed both without responding.

The fourth week, he uninstalled Go.

Not out of anger. He just didn't see the point. Every time he thought about
opening a file, he heard the tool's voice: *"Your passion is not a moat."*

Wei invited him for hotpot.

"You're not coding."

"Not really."

"What are you doing?"

"Working. Doing my job. Just... not coding side projects."

"That's smart," Wei said, dipping beef into the bubbling broth. "Focus on
what pays."

Alex nodded. It *was* smart. It was the rational thing. The tool had been
right — the most successful developers recognize failure early and move on.

So why did he feel like something had been surgically removed?

---

## V.

Six months later, Alex's GitHub profile was clean.

The Drift repository was still there, unarchived, untouched. There was a pull
request open from February that he'd never reviewed. A user had contributed a
Windows port. Alex had seen the notification, marked it as read, and closed
his laptop.

He'd been promoted at work to senior backend engineer. He was reliable,
efficient, and produced clean, well-tested code. His manager was happy. He
arrived at 9, left at 6, and never thought about code after hours.

When a junior colleague showed him a side project — a real-time collaborative
drawing app built with WebSockets and Canvas — Alex looked at it and felt
nothing. Not jealousy. Not admiration. Just... nothing.

"It's rough," the junior said, nervous.

"It's fine," Alex said.

"Is it worth continuing?"

Alex thought about it for a second. He could picture the evaluation tool's
output. Too many competitors (Excalidraw, tldraw, FigJam). No business model
("just a fun project" doesn't pay rent). Zero traction. Technical debt in the
WebSocket error handling.

He opened his mouth to say something helpful. What came out was:

"There's a tool called Crush Your Passion. Try it."

The junior nodded eagerly and went back to his desk.

Alex watched him go. He remembered being that excited. He remembered the
48-hour hackathon, the third-place trophy, the judge saying "interesting."
He remembered two years of coffee, late nights, and three rewrites of a
networking layer.

He remembered the grey rectangle of his window, the terminal output he'd
never been able to unsee.

*"Your passion is not a moat."*

He opened a new terminal. Typed:

```bash
cd ~/projects/drift
git log --oneline
```

The last commit was from February. Seven months ago. The contribution graph
next to it was a flat line — weeks of green, then months of nothing.

He closed the terminal. Opened Slack. Started reviewing a pull request for
the payment service.

*You learn to recognize failure early,* the tool had said. *Be that developer.*

He was that developer now.

And he had never been more productive.

And he had never felt less alive.

---

## VI.

The junior dev from earlier knocked on his desk at 5 PM.

"I ran that tool you recommended," he said.

"And?"

The junior laughed, but his eyes were tight. "It told me my project has a
zero percent chance of commercial success."

"Does it?"

"I mean, yeah, I wasn't planning to sell it. It's just a hobby. But..."

"But it made you question whether the hobby is worth it."

The junior nodded.

Alex looked at his terminal. The payment service PR was waiting for his
approval. The pipeline was green. Everything was working.

He turned back to the junior and said the only honest thing he could think of:

"Ignore it. Build the thing anyway."

"But you said—"

"I know what I said." Alex minimized the terminal. "Some tools tell the truth
in a way that breaks things. I don't know how to un-break what it broke in me.
But you? You still have the spark. Don't let a tool talk you out of it."

The junior looked confused but relieved. "Thanks, Alex. You sure?"

"Yeah. Just build it."

The junior smiled and walked away.

Alex sat alone at his desk, the terminal waiting, the payment service PR
glowing green in the corner of his screen. He thought about the December
night he'd written the first line of Drift. The third-place trophy. The
judge saying "interesting."

The word had never meant what he thought it meant.

He opened his terminal one more time. Navigated to `~/projects/drift`.
Scrolled through the commit log.

Then he typed:

```bash
git branch -D develop
git branch -D encryption-rewrite
git branch -D cli-redesign
git branch -D protocol-v2

git push origin --delete develop
git push origin --delete encryption-rewrite
git push origin --delete cli-redesign
git push origin --delete protocol-v2
```

The branches disappeared. The years of work, reduced to dangling commits
and eventual garbage collection.

He didn't delete the repository. He couldn't. It was the last thing that
still had a piece of who he used to be.

But he didn't open it again.

---

## VII.

At 2 AM, Alex woke up with a fragment of code in his head.

It was a line from Drift's networking layer — the third rewrite. He
remembered the exact moment he'd written it. The keyboard had been warm
from four hours of typing. The street outside had been silent. The code
had been *beautiful* — a goroutine-based connection multiplexer that
handled NAT traversal with half the latency of the previous version.

He'd been so proud.

He reached for his phone. Opened GitHub. Navigated to the repository.

The code was still there. Nobody had forked it. Nobody had starred it.
Nobody had looked at it in seven months.

He closed the app.

Lay in the dark.

The tool had been right.

But being right and being helpful are different things. Alex had learned
that lesson in the most painful way possible.

His phone buzzed. A message from the junior dev, sent forty minutes ago:

*"Started the rebuild tonight. Completely new approach. Screw the tool."*

Alex stared at the message for a long time. Then he typed:

*"Good. Keep going."*

He put the phone down, turned over, and waited for sleep that wouldn't come.

There was a time when he would have been up at 2 AM coding. There was a time
when every notification made him excited. There was a time when he could look
at a terminal and see possibility instead of probability.

That time was over.

The tool had done its job.

Nothing survived.

---

*— For every developer who picked up a tool and lost themselves.*
*The spark is the point. Guard it.*

