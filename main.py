from file_handling import *

sub_file = Subtitle(".srt")
file_extension = sub_file.get_file_extension()
open_subtitle_file(find_subtitle_file_with_extension(file_extension))
print("Debug : The active subtitle extension is : " + str(file_extension))

# self-notes
# dev-decide : do you want to pass filename strings or handles?
# timeline
# dev-complete : set/get a working directory
# dev-future : browse-able directory selector?
# dev-complete : get a list of all files in active dir
# dev-complete : filter the list to the relevant subtitle files ".srt"
# dev-future : handle dirs with more than one subtitle file
# dev-complete : print all contents from the selected text file
# dev-complete : print a selected line number from the selected text file
# dev-in-progress : print a selected line range from the selected text file
# dev-future : present a selectable input if more than one available file
# dev-future : present the option to shift subtitle forward or back in time
# dev-in-progress : present the option to input an integer time shift
# dev-future : present the option to input a decimal time shift

# end
