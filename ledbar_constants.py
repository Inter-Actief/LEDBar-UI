FADE_OPTIONS = [{
        'name': 'cyclic',
        'long_name': 'Cycle',
        'description': 'Cycles through all available options.',
    }, {
        'name': 'immediate',
        'long_name': 'Immediate',
        'description': 'Shows the text immediately.',
    }, {
        'name': 'open_right',
        'long_name': 'Scroll in from right',
        'description': 'Scrolls the text in from the right.',
    }, {
        'name': 'open_left',
        'long_name': 'Scroll in from left',
        'description': 'Scrolls the text in from the left.',
    }, {
        'name': 'open_from_center',
        'long_name': 'Open from center',
        'description': 'Scrolls the text in from the center to the edges.',
    }, {
        'name': 'open_to_center',
        'long_name': 'Open to center',
        'description': 'Scrolls the text in from the edges to the center.',
    }, {
        'name': 'cover_from_center',
        'long_name': 'Cover from center',
        'description': 'Shows the text from the center to the edges.',
    }, {
        'name': 'cover_from_right',
        'long_name': 'Cover from right',
        'description': 'Shows the text from the right to the left.',
    }, {
        'name': 'cover_from_left',
        'long_name': 'Cover from left',
        'description': 'Shows the text from the left to the right.',
    }, {
        'name': 'cover_to_center',
        'long_name': 'Cover to center',
        'description': 'Shows the text from the edges to the center.',
    }, {
        'name': 'scroll_up',
        'long_name': 'Scroll up',
        'description': 'Scrolls the text up from below.',
    }, {
        'name': 'scroll_down',
        'long_name': 'Scroll down',
        'description': 'Scrolls the text down from above.',
    }, {
        'name': 'interlace_center',
        'long_name': 'Scroll interlace',
        'description': 'Scrolls one half of the rows in from the left, one half from the right, '
                       'line by line.',
    }, {
        'name': 'interlace_cover',
        'long_name': 'Cover interlace',
        'description': 'Shows one half of the rows from the left, one half from the right, '
                       'line by line.',
    }, {
        'name': 'cover_up',
        'long_name': 'Cover upwards',
        'description': 'Show text line by line from the bottom upwards.',
    }, {
        'name': 'cover_down',
        'long_name': 'Cover downwards',
        'description': 'Show text line by line from the top downwards.',
    }, {
        'name': 'scan_line',
        'long_name': 'Scanline',
        'description': 'Let a scanline draw the text pixel by pixel.',
    }, {
        'name': 'explode',
        'long_name': 'Explode',
        'description': 'Show the text through an explosion on parts of the board.',
    }, {
        'name': 'pacman',
        'long_name': 'Pacman',
        'description': 'Let pacman eat the panel to uncover the text.',
    }, {
        'name': 'fall_stack',
        'long_name': 'Falling stack',
        'description': 'Let the text fall in from the top.',
    }, {
        'name': 'shoot',
        'long_name': 'Shoot',
        'description': 'Shoot the text in from the right, a few pixels at a time.',
    }, {
        'name': 'flash',
        'long_name': 'Flash',
        'description': 'Flash the text rapidly.',
    }, {
        'name': 'random',
        'long_name': 'Random transition',
        'description': 'Show random pixels of the text at random.',
    }, {
        'name': 'slide_in',
        'long_name': 'Slide letters in',
        'description': 'Slide each letter in one by one from the right.',
    }, {
        'name': 'auto',
        'long_name': 'Automatic',
        'description': 'Determine the fade effect automatically (similar to <code>"cyclic"</code>).',
    }
]

SPEED_OPTIONS = [
    {'name': 'default', 'long_name': 'Default (3)', 'description': "The default speed (same as <code>speed_3</code>)."},
    {'name': 'speed_1', 'long_name': 'Fastest (1)', 'description': "Fastest"},
    {'name': 'speed_2', 'long_name': '2', 'description': ""},
    {'name': 'speed_3', 'long_name': '3 (default)', 'description': "Default"},
    {'name': 'speed_4', 'long_name': '4 (do not use)', 'description': "<i>unreadable due to flickering, do not use</i>"},
    {'name': 'speed_5', 'long_name': '5 (do not use)', 'description': "<i>unreadable due to flickering, do not use</i>"},
    {'name': 'speed_6', 'long_name': '6 (do not use)', 'description': "<i>unreadable due to flickering, do not use</i>"},
    {'name': 'speed_7', 'long_name': '7 (do not use)', 'description': "<i>unreadable due to flickering, do not use</i>"},
    {'name': 'speed_8', 'long_name': 'Slowest (8)', 'description': "Slowest"},
]

COLOR_OPTIONS = [
    {
        'name': 'red',
        'long_name': 'Red',
        "description": "<span class='color'><code class='red'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'bright_red',
        'long_name': 'Bright Red',
        "description": "<span class='color'><code class='bright_red'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'orange',
        'long_name': 'Orange',
        "description": "<span class='color'><code class='orange'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'bright_orange',
        'long_name': 'Bright Orange',
        "description": "<span class='color'><code class='bright_orange'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'yellow',
        'long_name': 'Yellow',
        "description": "<span class='color'><code class='yellow'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'bright_yellow',
        'long_name': 'Bright Yellow',
        "description": "<span class='color'><code class='bright_yellow'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'green',
        'long_name': 'Green',
        "description": "<span class='color'><code class='green'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'bright_green',
        'long_name': 'Bright Green',
        "description": "<span class='color'><code class='bright_green'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'layer_mix_rainbow',
        'long_name': 'Rainbow',
        "description": "<span class='color'><code class='layer_mix_rainbow'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'bright_layer_mix_rainbow',
        'long_name': 'Bright Rainbow',
        "description": "<span class='color'><code class='bright_layer_mix_rainbow'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'vertical_mix',
        'long_name': 'Vertical Mix',
        "description": "<span class='color'><code class='vertical_mix'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'sawtooth_mix',
        'long_name': 'Sawtooth',
        "description": "<span class='color'><code class='sawtooth_mix'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'green_on_red',
        'long_name': 'Green-on-red',
        "description": "<span class='color'><code class='green_on_red'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'red_on_green',
        'long_name': 'Red-on-green',
        "description": "<span class='color'><code class='red_on_green'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'orange_on_red',
        'long_name': 'Orange-on-red',
        "description": "<span class='color'><code class='orange_on_red'>Lorem ipsum dolor sit amet.</code></span>"
    },
    {
        'name': 'yellow_on_green',
        'long_name': 'Yellow-on-green',
        "description": "<span class='color'><code class='yellow_on_green'>Lorem ipsum dolor sit amet.</code></span>"
    },
]

FONT_OPTIONS = [
    {'name': 'short', 'long_name': 'Short (5x6)', 'description': ""},
    {'name': 'short_wide', 'long_name': 'Short and Wide (5x11)', 'description': ""},
    {'name': 'default', 'long_name': 'Default (7x6)', 'description': ""},
    {'name': 'wide', 'long_name': 'Wide (7x11)', 'description': ""},
    {'name': 'serif', 'long_name': 'Serif (7x9)', 'description': ""},
    {'name': 'extra_wide', 'long_name': 'Extra Wide (7x17)', 'description': ""},
    {'name': 'small', 'long_name': 'Very Small', 'description': ""},
]
