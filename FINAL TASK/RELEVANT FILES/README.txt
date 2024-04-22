SO here's a breif of how I went about my task. 

1. Spawned balls on the provided game field (areaurdf_noarea1 package) (created a parser file to parse the urdf correctness)
2. Used the differential_drive_robot packages and installed a camera plugin on top of it and integrated the launch files of the two packages (areaurdf_noarea1 and differential_drive_robot) to have the bot run on my game field.
3. then I created a node called ball_detector to detect balls and silos on the field. It detected the balls just fine but would detect multiple circles concentrated inside the silo instead of a rectangular detection.
4. couldn't get to the transform publishing part. 
