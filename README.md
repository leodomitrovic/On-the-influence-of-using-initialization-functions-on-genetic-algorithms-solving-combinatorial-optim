# On-the-influence-of-using-initialization-functions-on-genetic-algorithms-solving-combinatorial-optim
Topic: On the influence of using initialization functions on genetic algorithms solving combinatorial optimization problems: a first study on the TSP
Source code on topic written by 4th year computer science students Leo Domitrović and Ingo Kodba. Original research by E. Osaba; R. Carballedo; F. Diaz; E. Onieva; P. Lopez; A. Perallos.

To start immediately, run initialize.py. Implemented algorithms in hfunctions.py are order crossover, 50% random elitism, roulette wheel selection, two opt.
Two opt gives us the most trouble because it takes the most time to calculate. We used Ray.io library to enable computation on multiple CPU cores, shortening the time of execution.
There are many files that help with testing algorithms or logic, or just calculate stuff, they are: just_one_city.py, test_twoopt.py, initialize_test.py, how_many_results_until_now.py, calculate_distances.py, download_cities.py, draw_timeline.py.
Results and times of execution are numpy array saved in data.npy and times.npy, respectively.

By running this experiments, we found out that initialization functions don't significantly influence time or results, as opposed to original research.

Project includes many unnecessary files such as backups during development, Word documents of explinations in croatian language and images of sketches.
All variable names are translated from croatian to english for broader audience. Comments are mostly untranslated.
We hope this repository helps you if you want to study similair projects.
You can freely apply commits to improve this project.
