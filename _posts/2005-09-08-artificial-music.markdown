---
author: vitraag
comments: true
date: 2005-09-08 05:54:00+00:00
layout: post
link: https://vitraagblog.wordpress.com/2005/09/07/artificial-music/
slug: artificial-music
title: Artificial Music
wordpress_id: 1070
categories:
- music
---

My rendition of Alap in Raag Bhup with Teen-taal in beats, the code is in lisp:

(setq _BHUP-SCALE_ '(55 57 59 60 62 64 65 67 69
71 72 73 75 76))
(setq _TEEN-TAAL-THEKA_ '((0 45 500 10 127)
(500 41 500 10 127)
(1000 41 500 10 127)(1500 45 500 10 127)))

(defun compose (number-of-events ontime)
"(compose 77 0)"
(if (zerop number-of-events)()
(cons (list ontime
(+ (choose-bhup-notes 0) 0)
;;to put it in MIDI range
1000
1
127)
(compose (- number-of-events 1)
(+ ontime 1000)))))

(defun surleena (number-of-events)
"Alap with zor n zhala optimum @ 25 events"
(let
((alap (long-notes
(compose number-of-events 0) 0))
(zor-zhala (scale-tempo 0.5
(compose number-of-events 0)))
(zor-theka (scale-tempo 1
(repeat-events 8 2000
_TEEN-TAAL-THEKA_))))
(append
alap
(shift-ontime
(* 1000 number-of-events) zor-zhala)
(shift-ontime
(* 500 number-of-events) zor-theka)
))
)

(defun long-notes (events change-so-far)
"Assuming events are well-formed"
(if (null events) ()
(let ((change (random 500)))
(cons (change-tempo (first events)
change-so-far change)
(long-notes (rest events)
(+ change change-so-far))))))

(defun change-tempo (event val tempo)
"(change-tempo '(0 34 1000 1 127) 0 500) returns
'(0 34 1500 1 127)"
(list (+ (nth 0 event) val)
(nth 1 event)
(+ (nth 2 event) tempo)
(nth 3 event)
(nth 4 event)
)
)

(defun choose-bhup-notes (number)
"Picks one note from a flute based bhup scale"
(let ((val (+ (random 23) 53)))
(cond
((memberp val _BHUP-SCALE_) val)
(t (choose-bhup-notes number))
))
)

(defun memberp (elem elist)
"Is elem a member of elist"
(cond
((= elem (first elist)) t)
((null (rest elist)) ())
((not (null elist))
(memberp elem (rest elist)) )
)
)

(defun scale-tempo (factor events)
"Scales tempo 0-1 1 implies no effect"
(if (null events) ()
(let* ((event (first events))
(ontime (round
(* factor (first event))))
(duration (round
(* factor (third event)))))
(cons
(list ontime (second event)
duration
(fourth event) (fifth event))
(scale-tempo factor (rest events))
)))
)

Enjoy the code is LGPL.
