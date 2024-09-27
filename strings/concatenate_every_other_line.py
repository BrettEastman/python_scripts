def process_text(input_text):
    lines = input_text.split('\n')
    result = []
    for i in range(1, len(lines), 2):
        result.append(lines[i])
    return ' '.join(result)


# Example usage
input_text = '''
statistically 96% of the humans watching
0:03
this video are not using Linux and
0:05
that's just like really sad because it's
0:06
a superior free open source operating
0:09
system but only has a 4% share of the PC
0:11
market luckily though 96% of the
0:14
non-human Bots watching this video are
0:16
using Linux because it is the dominant
0:18
OS on the server if you're a programmer
0:20
or developer you need to know Linux
0:22
that's where your code will eventually
0:24
run and fail and if you can't SSH into a
0:26
Linux terminal and fix it you are
0:28
screwed in today's video you'll learn
0:30
everything you need to know about Linux
0:31
by looking at 101 essential Concepts
0:34
over the next 10 minutes if you survive
0:36
until the end you should magically grow
0:37
neck beard and be able to technobabble
0:40
like an arch user before one can
0:42
understand Linux though one must
0:43
recognize what came before it Unix an
0:45
operating system developed at AT&T Bell
0:48
labs in the 70s its development led to a
0:50
standardization called posix or portable
0:53
operating system interface to ensure
0:55
that different systems would be
0:56
compatible with each other its influence
0:58
remains strong today with m ma OS
1:00
Android FreeBSD and most Linux dros
1:03
being posix compliant in 1987 an OS
1:06
called Minix for academic use was
1:08
developed but redistribution of its code
1:10
was restricted this inspired a Finnish
1:11
computer science student named lonus
1:13
torald to develop Linux in 1991
1:16
importantly it's free open- source
1:18
software licens under GPL 2.0 and by
1:21
free I mean free is in Freedom it's free
1:23
to distribute modify and make money off
1:25
of now what I'm referring to as Linux is
1:27
in fact not an operating system but
1:29
rather an operating system kernel it's
1:31
written in the C programming language
1:33
and is the black magic that sits between
1:35
your software applications and the
1:37
hardware when you hit the power button
1:38
on your computer the boot loader which
1:40
is usually grub will load the Linux
1:42
kernel into random access memory from
1:44
there it detects hardware and starts the
1:46
init system which is typically a tool
1:48
called system D although Alternatives do
1:50
exist once initialized the kernel will
1:52
start up applications in user space
1:54
which will typically bring the user to a
1:56
login screen as the user starts doing
1:58
stuff the konel has a lot of respons
1:59
ibility it allocates and deallocates
2:01
memory for processes and can even create
2:04
virtual memory to use more memory than
2:06
is physically available by tapping into
2:08
your hard drive speaking of the hard
2:09
drive the kernel also provides a virtual
2:12
file system to interact with files on
2:14
different systems the fourth extended
2:16
file system is the most common default
2:17
on Linux but it's not the only option
2:20
the kernel also interacts with all these
2:21
peripheral devices via drivers pretty
2:24
cool but you can't just walk up and mess
2:26
around with the kernel and that's
2:27
because it's surrounded by the cpu's
2:29
protection ring at ring zero we have the
2:31
kernel with the highest level of
2:33
privilege While most of us normies in
2:34
user space live in ring three with the
2:36
lowest level of privilege but often
2:39
you'll want to do something that
2:40
requires access to the kernel like write
2:42
a file to the file system and that's
2:44
where system calls come in in the C code
2:46
here you'll notice that I'm making a CIS
2:48
call to write which will transition from
2:50
ring three to ring zero to Output some
2:53
text to the console however right itself
2:55
is not a system call it's actually a
2:57
rapper provided by GBC which is the G
3:00
new standard library for C and provides
3:02
all kinds of rappers for making system
3:03
calls that can do almost anything on
3:05
your OS but wait a minute what is gnu
3:08
it's pronounced gnu and it's a project
3:10
that predates the Linux kernel itself
3:12
and was started all the way back in 1983
3:14
by Richard stalman it provides all the
3:16
core utilities for Linux which are all
3:18
the software utilities that make the
3:19
kernel useful to humans the best way to
3:21
start exploring these core Libs is to
3:23
open up the terminal which is a
3:25
graphical user interface that allows you
3:26
to send commands via the shell now they
3:28
call this thing a shell because it
3:30
provides a layer of protection between
3:32
user space and the kernel there are many
3:34
different flavors of shells but the most
3:36
common is Bash let's say hello to the
3:38
Linux kernel by running the ganu shell
3:40
utility Echo and providing a string
3:42
argument to it this command takes our
3:44
message and prints it to the standard
3:46
output pretty simple but what actually
3:48
happened under the hood is that a system
3:50
call was made to the kernel which
3:52
checked permissions and manage drivers
3:54
to turn those ones and zeros into pixels
3:56
on the screen as an end user though I
3:58
don't care my friend told me about a
4:00
cool command called touch but I have no
4:02
idea what it does the cool thing about
4:03
Linux is that you can pull up the manual
4:05
for any command by hitting up my main
4:07
man man it looks like this command is
4:10
used to create a new file man Isn't that
4:12
cool let's go ahead and try it out now
4:13
by creating a new text file it looks
4:15
like nothing happened but I promise it
4:17
worked I can prove it by using the ls
4:19
command to list out the files in this
4:21
directory and there it is and we can
4:23
read the file contents with the cat
4:25
command but again nothing happens
4:26
because there's no data in this file
4:28
however there is a bunch bunch of
4:30
metadata like timestamps that we can
4:32
access with the stat command is stat
4:34
rhymes with cat and when we run it we
4:35
know this file's birth time when it was
4:37
modified and when it was last accessed
4:39
that's useful but we can also get more
4:41
information from the ls command by
4:43
appending Flags to it like the L flag to
4:46
list more details and the H flag to make
4:48
them human readable when we run that
4:50
command we can now see the exact size of
4:52
every file and we can also combine flags
4:54
and Linux to make this command more
4:56
concise I don't want an empty file
4:57
though so I'm just going to remove it
4:59
with the RM command the cool thing about
5:01
the Linux terminal is that it's really
5:03
easy to combine commands like I can take
5:05
Echo and use this angle bracket to
5:08
redirect its output to a new file in
5:10
addition I can flip this angle bracket
5:12
around to also redirect the input of a
5:14
file that's cool but pipes are even
5:16
cooler they allow you to take the output
5:18
of one command and pass it off to
5:20
another command like for example if we
5:22
have a log file of our broken code we
5:24
might first use cat to read that file
5:26
but then we could pipe the output to
5:28
sort which would sort it line by line
5:30
and then unique to remove any duplicates
5:32
there's so much more we could do just
5:33
from the terminal but if you find
5:35
yourself doing the same thing over and
5:36
over again it might be time to write a
5:38
bash script in its own dedicated file
5:40
but to create that file we'll use an
5:42
interactive text editor if you have a
5:44
few years to spare you could try
5:45
learning Vim or if you have no life at
5:47
all you could try emac but I'm going to
5:49
create this file with Nano a minimal
5:51
text editor built into most Linux dros
5:53
at the top of the file We'll add a
5:55
shebang that tells Linux to use the bash
5:57
interpreter then we can add as much bash
5:59
code as we want here like we might use
6:01
Echo and then read to read a value from
6:03
the standard input and then Echo to once
6:05
again Echo it back and now if we save
6:07
this file we can execute it by simply
6:09
entering the file path in the terminal
6:11
and that brings us to the halfway mark
6:13
unfortunately 100 topics is not nearly
6:15
enough to cover the entire Linux
6:17
ecosystem if your goal is to become an
6:19
apex Alpha Linux gigachad and check out
6:21
my brand new full Linux course for
6:23
fireship pro members the course contains
6:25
over 30 videos of Hands-On Linux topics
6:27
along with quizzes for regular dopamine
6:29
hits that will help you master the
6:31
fundamentals of Linux quickly but most
6:33
importantly it will teach you how to
6:34
spin up your own virtual private server
6:36
to self-host your own applications but
6:38
one major drawback of using Linux is
6:40
that it might trigger an existential
6:42
crisis and you might ask yourself who am
6:44
I when you enter that command it's going
6:45
to return your Linux username in
6:47
addition every user has a unique uid
6:50
that can be viewed with the ID command
6:52
my ID is 1000 but there is one special
6:54
user with a uid of zero called root AKA
6:58
admin super user or daddy root has the
7:00
highest level of privilege and you can
7:02
switch to the root user with the Su
7:04
command or prefix any command with
7:06
pseudo to run it with elevated privilege
7:08
any user can be granted pseudo privilege
7:10
and you can check your privilege right
7:11
now by running pseudo flag l in addition
7:14
to users Linux also has groups groups
7:17
have group IDs and make it easier to
7:18
manage permissions for multiple users
7:21
before we talk about permissions though
7:22
let's explore the file system by default
7:25
we're in our home directory which is
7:26
like a personal workspace for the user
7:28
you're logged in as we might make a new
7:30
directory here using the make dur
7:32
command then use CD to change
7:34
directories into it now run PWD to print
7:37
the current working directory but now
7:38
let's venture outside of our home into
7:40
the root of the file system by running
7:42
cd/ if you hit LS here you'll find a
7:44
bunch of critical directories that you
7:46
need to know aot like boot contains the
7:48
Linux kernel itself Dev contains
7:50
external devices like hard drives Etc
7:53
contains config files and VAR contains
7:55
log files the most interesting directory
7:57
here though is bin which holds your
7:59
binaries and spin for system binaries
8:02
you see when you run a command like LS
8:04
Linux looks for an executable binary on
8:06
your system to execute the thing is
8:09
binaries not only live here but also
8:11
under the user system Resources
8:13
directory and potentially anywhere you
8:15
want on the file system and that begs
8:16
the question how does Linux know where
8:18
to find the right binary well that's
8:20
where path comes in it's a special
8:22
environment variable that contains paths
8:24
to directories separated by colons when
8:27
you enter a command Linux will search
8:29
through the path for a matching binary
8:30
in each directory and execute the first
8:33
one it finds its value is set on the
8:34
system by default but it's common to
8:36
customize it by using the export keyword
8:39
which will set the value for an
8:40
environment variable the most common
8:41
technique is to update the path for an
8:43
individual user by customizing The Bash
8:46
RC file which itself is a script that
8:48
will run before every terminal session
8:50
and now that we're inside this file we
8:51
can also do things like customize the
8:53
PS1 environment variable to change the
8:55
terminal prompt to look more like a mega
8:57
hardcore hacker when coding at Starbucks
8:59
which is a proven way to attract a mate
9:01
as a Linux user but now it's time to
9:03
talk about file permissions use LS flag
9:05
L on any file to view permissions and
9:07
notice these cryptic nine characters
9:10
these are called symbolic permissions
9:12
the first triplet represents the owner
9:14
the middle the group and the last
9:15
triplet is for everyone else each one
9:17
contains a letter that represents read
9:20
write and execute privileges if the
9:21
letter is present it means access
9:23
granted but if there's a dash it means
9:25
permission denied these can also be
9:27
represented as numbers in o notation for
9:30
example 777 lets anybody do anything to
9:33
a file I know Triple 7 is good on slot
9:35
machines but in Linux it's generally a
9:38
bad idea because you want to always
9:39
follow the principle of lease privilege
9:41
Grant access to things only when
9:43
necessary and trust no one now you can
9:45
modify the permissions on a file with
9:47
the chamod command like here I'm using
9:49
it to Grant read access to a document
9:51
for everybody we can also change the
9:52
owner of a file with Chon or assign
9:55
groups with ch group and now that we
9:57
know what all these things mean
9:58
permissions aren't so cryp now anytime
10:00
you run a command or execute a program
10:02
it creates a process on the CPU which is
10:04
managed by the Linux kernel you can view
10:06
these processes with a command and
10:08
notice how each one has a unique process
10:10
ID along with the user who created it or
10:13
better yet use htop to get an
10:15
interactive breakdown of processes that
10:17
can be filtered some of these are just
10:18
system demons that run in the background
10:20
we all have our demons in fact if you
10:22
have a long running script you can even
10:24
create your own background process by
10:26
adding an Amper sand to the end of it or
10:28
if you want a a script run on a specific
10:30
schedule like a reminder to do something
10:32
at 4:20 p.m. today you can accomplish
10:34
that by adding your script to the cron
10:36
tab that's cool but occasionally you'll
10:38
have a bad process that needs to be
10:39
killed the kill command can do that by
10:42
gracefully sending a Sig term signal to
10:44
the process if that doesn't do the trick
10:46
though use the nine flag to forcefully
10:48
kill it with Sig kill we've barely
10:50
scratched the surface but so far
10:52
everything we've looked at is pretty
10:53
standard on most Linux machines other
10:55
utilities you should know about include
10:57
GP for searching through text said for
10:59
modifying tax gzip for making files
11:02
smaller and tar for archiving
11:04
directories but the Linux experience
11:06
varies wildly when talking about
11:07
different dros a Linux distribution is
11:10
just a complete operating system built
11:12
on the Linux kernel and each drro has a
11:14
highly opinionated set of default
11:16
software for their target audience some
11:18
are designed for beginners others for
11:20
hardcore hackers and everything in
11:22
between dros can have different package
11:24
managers to install new software like a
11:27
yum and Pac-Man and they might also have
11:29
different release schedules like some
11:31
have a predictable fixed release date
11:32
While others have ruling releases that
11:34
keep their software on The Cutting Edge
11:36
at all times and one thing we didn't
11:37
even talk about is desktop environments
11:39
if using Linux as a PC your Dro will
11:42
have a default desktop environment like
11:44
gnome or KD plasma and that makes a huge
11:46
difference in the experience some distro
11:48
families you should know about include
11:50
slackware the Original Gangster from the
11:52
9s Debian the most popular Dro overall
11:55
famous for its open philosophy and ease
11:57
of use red hat the dro of choice and
11:59
Enterprise for its long-term support
12:01
plans and finally the arch family if
12:04
someday you find yourself saying I use
12:05
Arch by the way unironically it means
12:07
you've embrace the Paradox of complexity
12:09
and simplicity and your operating system
12:12
is no longer just a tool but a
12:13
reflection of your own dominance and
12:15
Mastery over the digital world thanks
12:17
for watching check out the full course
12:19
if you want to go deeper and I will see
12:20
you in the next one
'''

output = process_text(input_text)
print(output)
