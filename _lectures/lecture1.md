---
layout: with-sidebar
index: 1
name: Course Intro + Logistics + Hello World
released-on: "2024-04-01"
videos:
    - title: "What is CSE 8A?"
      url: https://drive.google.com/file/d/1dTXFLjJ22hrm14pND1DrULQsJlyM10WY/view?usp=drive_link
    - title: "Hello World"
      url: https://drive.google.com/file/d/1dEIJ6ZKpUKt63n8FvCGioKYyr6lI8TrK/view?usp=drive_link
---

## Problem Session 1 – Course Intro + Logistics + Hello World

_{{ page.released-on }}_

Welcome to the page for the first lecture! Each lecture will
come with a page like this that summarizes the videos you should watch and
readings you should complete **beforehand**, along with any handouts for the day
as well as code examples and notes from the leture.

The university requires us to determine which students commence academic activity. Failure to certify academic activity, may result in students being billed for unearned financial aid.

To do this automatically, we are using a survey in Canvas that every student must fill out by the end of Friday of Week 2 to ensure that they are certified.
- [First Day Survey: Tell Me About Yourself #FinAid](https://canvas.ucsd.edu/courses/54799/quizzes/170078){:target="_blank"}

After the first lecture, there is one video to watch. You should also familiarize
yourself with the [syllabus](../syllabus.html).

Videos (to watch **after** lecture):

{% for video in page.videos %}
[{{ video.title }}]({{ video.url }}){:target="_blank"}

<iframe src="{{ video.url }}/preview" width="640" height="480" allow="autoplay"></iframe>
{% endfor %}

## Notes & Files from Pre-Lecture Videos

[Pre-Lecture 1](https://github.com/ucsd-cse8a-sp24/ucsd-cse8a-sp24.github.io/tree/main/_pre-lectures/lecture-01){:target="_blank"}

## Notes & Files from Lecture 

[Lecture Notes](https://drive.google.com/drive/folders/121Wc9zxLJsLy3bH9RmB5UstuCu2X37zc?usp=sharing){:target="_blank"}
