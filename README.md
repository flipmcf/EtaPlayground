# EtaPlayground
Just playing with logging time and ETA of long running processes

it's not hard.

Let's make loop where we sleep and interate over it a bunch of times.
We record the start and end, average up the time it takes to do each loop iteration, then compute an estimate on now long it will take to complete the rest of the iteations.

    python eta_play.py <iterations> <sleep time>  [--sigma]


running it with witout a _sigma_ option will just sleep for _sleep time_ seconds and it's pretty broing.

adding a _sigma_ will create a normal distribution around _sleep time_ to get a more random behavior.

Read the code, use it as an example, and enjoy life.
