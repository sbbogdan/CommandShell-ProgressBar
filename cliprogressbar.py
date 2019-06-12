# Progress Bar for use with command line tools
import datetime, time

class CliProgressBar:

	# progress bar characters
	progress_chars = ['░', '▒', '▓', '█']

	# constructor; set progress characters
	def __init__(self):
		self.reset()

	# display latest progress to console
	def display_progress(self, percent_complete=0):
		# throw exception if value not between 0 and 1
		if not (0 <= percent_complete <= 1):
			raise Exception('\'percent_complete\' parameter value must be between 0 and 1, inclusive.')

		# determine what percentage of the progress bar is full, empty
		filled_progress = int(percent_complete * 100 // 2)

		# reserve one character for the current/progress character; hence 49 and not 50
		empty_progress = 49 - filled_progress 

		# set and determine new 'current progress' char
		if self.progress_last_fill == filled_progress:
			self.progress_char_state = (self.progress_char_state + 1) if self.progress_char_state < 2 else 0
		elif filled_progress == 50:
			self.progress_char_state = 3
		else:
			self.progress_char_state = 0

		self.progress_last_fill = filled_progress
		progress_char = self.progress_chars[self.progress_char_state]

		# create progress bar
		progress_bar = self.progress_chars[3] * (filled_progress) + progress_char + u'-' * (50 - int(percent_complete  * 100 // 2))

		percent_complete_string = '{:,.2f}'.format(percent_complete * 100)

		print('Progress: |{}| {}% Complete ({} Remaining)'.format(progress_bar, percent_complete_string, self.calculate_remaining_time(percent_complete)), end='\r')

	# get remaining time
	def calculate_remaining_time(self, percent_complete=0):

		# get past two percent before displaying a predicted remaining time
		if percent_complete > 0.02:

			# get current time
			current_time = time.time()

			# calculate change in time
			change_in_time = (current_time - self.last_update_time) 

			# calculate average time per 0.01% advancement
			self.collective_time_total += change_in_time #seconds

			# if no advancement, display last remaining time; else calculate new remaining time
			if percent_complete != 0:
				time_per_increment = self.collective_time_total / (percent_complete * 1000)

				remaining_time = str(datetime.timedelta(seconds=((1 - percent_complete) * 1000 * time_per_increment))).split(':')
				self.remaining_time = '{}h:{}m:{}s'.format(remaining_time[0], remaining_time[1], remaining_time[2].split('.')[0])

			# set last_update_time to current_time
			self.last_update_time = current_time

		# return remaining_time string
		return self.remaining_time

	# reset progress bar (variables) to 0/start
	def reset(self):
		# last char state, last_fill - used for progress spinner
		self.progress_last_fill = 0
		self.progress_char_state = 0

		# last_update_time, remaining_time, etc. - used for remaining time calculation
		self.last_update_time = time.time()
		self.collective_time_total = 0
		self.remaining_time = '*h:**m:**s'
