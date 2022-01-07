import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import tkinter as tk
import tkinter.font as font
"""
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'6892',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'a80e718a-61fa-4358-80c0-14b3cbcae1bd',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    oeuf = json.loads(response.text)
    #with open('test.json', 'w') as file:
    #    caca=json.dumps(data, indent=2)
    #    file.write(caca)
    #print(data)
    print(oeuf["data"]["6892"]["name"])

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)



def current(args=str):
  
  print("it's a me!")
  try:
    cmoplete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+f"{args}"+"&appid=6e2d2db27e5a42fa384a698d859fc686"
    api_link=requests.get(cmoplete_api_link)
    api_data=api_link.json()
    print(cmoplete_api_link)
  except requests.exceptions.RequestException as e:
    print(e)
  if api_data['cod']=='404':
    print("hey fuck off that's not the right city")
  else:
    temperature=((api_data['main']['temp'])-273.15)
    windspeed=((api_data['wind']['speed'])*3.6)
    city = f'{args}\'' if args[-1]=='s' else f'{args}\'s'
    fahr=9.0/5.0 * temperature + 32
    print(f"{temperature}°C and {fahr}F")
  print(city)


current("Guérande")
"""

with open("C:\\Users\\ARyOtaRe\\Documents\\SlashBot\\en.json", encoding="utf8") as en_json:
  en_data=json.loads(en_json.read())

#with open("C:\\Users\\ARyOtaRe\\Documents\\SlashBot\\TEMPLATE.json", encoding="utf8") as template_json:
  #template_data=json.loads(template_json.read())



template_data={
    "CLICK_TO_ARCHIVE_THREAD": "Click below to archive this thread",
    "SWITCH_ROLE": "Switch role \"{0}\"",
    "TOGGLE_ROLE": "Toggle role \"{0}\"",
    "ADD_ROLE": "Add role \"{0}\"",
    "REMOVE_ROLE": "Remove role \"{0}\"",
    "UNSUPPORTED_FORMAT": "Unsupported format",
    "SLASHBOT_DEVELOPER": "SlashBot Developer",
    "MESSAGEINFO_TITLE": "MessageInfo",
    "EVENTS_RECEIVED": "Events received",
    "SUPPORT_SERVER": "Support Server",
    "PREMIUM_STATUS": "Premium status",
    "OPEN_PRIVATE_THREAD": "Open a private thread",
    "OPEN_PUBLIC_THREAD": "Open a public thread",
    "PRONOUN_ROLES": "Pronoun Roles",
    "DISPLAY_ROLES": "Display your roles",
    "SERVER_RULES": "Show Server Rules",
    "SOMETHING_ELSE": "Something else",
    "PRIVATE_THREAD": "Private thread {0}",
    "CREATED_THREAD": "Created thread {0}",
    "OTHER_DROPDOWN": "Other Dropdown",
    "ARCHIVE_THREAD": "Archive thread",
    "IMAGE_QUALITY": "Image quality",
    "SLASHBOT_USER": "SlashBot User",
    "SELECT_OPTION": "Select one of the options",
    "REMOVED_ROLES": "Removed Roles",
    "SELECT_A_ROLE": "Please select a role below",
    "DELETE_THREAD": "Delete thread",
    "INFO_SHARDID": "ShardID",
    "GUILD_AVATAR": "Guild Avatar",
    "GUILD_BANNER": "Guild Banner",
    "SHARD_GUILDS": "Shard Guilds",
    "TOTAL_SHARDS": "Total Shards",
    "NEEDED_ROLES": "Needed Roles",
    "SELECT_ROLES": "Select one of the {0} roles",
    "SELECT_BELOW": "Please select below",
    "WARN_SUCCESS": "**{0} has been warned for:**\n{1}{2}",
    "KICK_SUCCESS": "**{0} has been kicked for:**\n{1}{2}",
    "MUTE_SUCCESS": "**{0} has been muted for:**\n{1}\nThey will be unmuted <t:{2}:R>{3}",
    "UNMUTE_SUCCESS": "**{0}** has been unmuted by {1}",
    "WARN_SUCCESS_REASONLESS": "**{0} has been warned**",
    "IMAGE_FORMAT": "Image format",
    "PLACEHOLDER_TEXT": "Do you like dogs?",
    "BAN_SUCCESS": "**You've been banned from __{0}__ for:**\n{1}",
    "LOADING": "<a:loading:773778301629235202> Please wait...",
    "CONTEXT_MENUS": "Context Menus",
    "COMPONENTS": "Components",
    "COMMANDS": "Commands",
    "COMMAND": "Command",
    "VIEW_IN_WEB": "View in Web",
    "PERMISSIONS": "Permissions",
    "INFO_UPTIME": "Online since",
    "TRANSFERRED": "Transferred",
    "NO_PREMIUM": "No Premium",
    "NO_CONTENT": "No content",
    "NO_REASON": "No Reason",
    "ENABLED": "enabled",
    "DISABLED": "disabled",
    "MESSAGE": "Message",
    "RAM_USAGE": "Ram usage",
    "WEBSITE": "Website",
    "PATREON": "Patreon",
    "CREATED": "Created",
    "RESET": "reset",
    "ASSETS": "Assets",
    "COPIED": "Copied",
    "GUILDS": "Guilds",
    "INVITE": "Invite",
    "JOINED": "Joined",
    "NOTIFY": "Notify",
    "AVATAR": "Avatar",
    "BANNER": "Banner",
    "GUILD": "Guild",
    "USERS": "Users",
    "ROLES": "Roles",
    "PING": "Ping",
    "VOTE": "Vote",
    "NONE": "none",
    "TYPE": "Type",
    "HOUR": "hour",
    "HOURS": "hours",
    "MINUTE": "minute",
    "MINUTES": "minutes",
    "SECOND": "second",
    "SECONDS": "seconds",
    "RULE": "Rule",
    "AND": "and",
    "OR": "or",
    "YES": "Yes",
    "NO": "No",
    "ERROR_EMBED_TEXT_OR_IMAGE_REQUIRED": "You need at least one text field or an image",
    "ERROR_EMOJI_IS_UNICODE": "I can't show information about unicode emojis",
    "ERROR_EMOJI_NOT_CUSTOM": "That doesn't seem like a custom discord emoji",
    "ERROR_UNABLE_TO_ADD_EMOJI": "I'm not able to add any emojis.",
    "ERROR_PROMPT_EXPIRED": "This prompt expired",
    "ERROR_COMPONENT_CREATED_BY_CLIENT": "I can only remove components that have been added by a user",
    "ERROR_EITHER_LABEL_OR_EMOJI": "You either have to have an emoji or a label",
    "ERROR_LABEL_LENGTH_EXCEEDED": "Your label exceeded the max length (max. 100)",
    "ERROR_DESCRIPTION_LENGTH_EXCEEDED": "Your description exceeded the max length (max. 100)",
    "ERROR_PLACEHOLDER_LENGTH_EXCEEDED": "Your placeholder exceeded the max length (max. 100)",
    "ERROR_BUTTONROLE_BUTTON_LIMIT_REACHED": "You can't add any more ButtonRoles to this message",
    "ERROR_BUTTON_LIMIT_REACHED": "You can't add any more Buttons to this message",
    "ERROR_DROPDOWN_LIMIT_REACHED": "You can't add any more Dropdowns to this message",
    "ERROR_CLIENT_MISSING_ROLE_PERMISSIONS": "I'm missing permissions to manage your roles",
    "ERROR_BUTTONROLE_MISSING_PERMISSIONS": "I'm missing permissions to update your roles",
    "ERROR_BUTTONROLE_ROLE_NAME_EXCEEDED": "Your role names can't be longer than 50 characters when not providing a custom label",
    "ERROR_TARGET_CLIENT_UNMANAGEABLE": "I'm not able to moderate this member",
    "ERROR_BUTTONROLE_MISSING_ADMIN": "You can't set up roles above you without administrator",
    "ERROR_BUTTONROLE_MISSING_ROLE1": "<:SystemMessageInteractionFail:872222564557127680> You're missing the role <@&{0}> to {1} the role(s) {2} {3} yourself.",
    "ERROR_BUTTONROLE_MISSING_ROLE2": "<:SystemMessageInteractionFail:872222564557127680> You're missing the role <@&{0}> to add the role(s) {1} to yourself.",
    "ERROR_BUTTONROLE_MISSING_ROLE3": "<:SystemMessageInteractionFail:872222564557127680> You're missing the role <@&{0}> to remove the role(s) {1} from yourself.",
    "ERROR_BUTTONROLE_MISSING_ROLE4": "<:SystemMessageInteractionFail:872222564557127680> You're missing the role <@&{0}> to switch out the role <@&{1}> for the role <@&{2}>.",
    "ERROR_BUTTONROLE_MISSING_ROLE5": "You don't have the role <@&{0}>, so I can't switch it out.",
    "ERROR_BUTTONROLE_TOO_MANY_ROLES": "When restricting the roles you can only set up 4 roles at once",
    "ERROR_BUTTONROLE_INVALID_REQUIRING_ROLE": "The requiring role is invalid",
    "ERROR_BUTTONROLE_REQUIRE_EVERYONE": "You can't require the @everyone role",
    "ERROR_BUTTONROLE_ALREADY_HAVE": "You already have the role(s): {0}",
    "ERROR_BUTTONROLE_DONT_HAVE": "You don't have any of the following role(s): {0}",
    "ERROR_BUTTONROLE_LABEL_REQUIRED": "When using more than 1 role a custom label is required",
    "ERROR_BUTTONROLE_EVERYONE_ROLE": "You can't hand out the `@everyone` role",
    "ERROR_BUTTONROLE_EVERYONE_SET_UP": "You can't set up the @everyone role",
    "ERROR_BUTTONROLE_DUPLICATE_SET": "This exact set of roles has already been given. You can't have duplicates.",
    "ERROR_BUTTONROLE_CANT_RESTRICT_TO_EVERYONE": "You can't set up the @everyone role as a restriction",
    "ERROR_FUNCTIONBUTTON_NO_PRONOUN_ROLES": "You need 4 roles called 'he/him', 'she/her', 'they/them' and 'others'",
    "ERROR_FUNCTIONBUTTON_USED_IN_THREAD": "You can't open threads in threads",
    "ERROR_INVALID_EMOJI_COMPONENTS": "There are invalid emojis in one or more components or there's already a button with the exact same set of roles on this message",
    "ERROR_MESSAGE_EDIT_FAIL": "There are invalid emojis in one or more components",
    "ERROR_MESSAGE_EDIT_FAIL_URL": "That's not a supported url or something else went wrong",
    "ERROR_BUTTONROLE_MANAGED_ROLE": "You can't hand out managed roles",
    "ERROR_SLOWMODE_TOO_LONG": "The please provide a total duration of 6 or less hours and more than 0 seconds",
    "ERROR_BANNED_MEMBER_NOT_FOUND": "I'm not able to find the banned member you want to unban",
    "ERROR_MAX_DURATION_ACTIVITIES": "The max is 7 days (604800 seconds)",
    "ERROR_COPYMESSAGE_NO_CONTENT": "I'm only able to copy messages with content or embeds",
    "ERROR_COPYMESSAGE_OTHER_BOT": "I can't copy components from other bots",
    "ERROR_SAY_TEXT_TOO_LONG1": "Your text can't be longer than 75 characters",
    "ERROR_SAY_TEXT_TOO_LONG2": "Your text can't be longer than 95 characters",
    "ERROR_NOT_A_VOICE_CHANNEL": "That's not a voice channel",
    "ERROR_TARGET_UNMANAGEABLE": "You can't moderate members above you",
    "ERROR_INVALID_MESSAGE_URL": "That's not a valid message URL",
    "ERROR_INVALID_MESSAGE_URL_OLD": "That's not a valid message URL (old)",
    "ERROR_INVALID_MESSAGE_URL_NEW": "That's not a valid message URL (new)",
    "ERROR_EMBED_INVALID_POSITION": "You can't put an embed at that position",
    "ERROR_INVALID_URL": "That's not a valid URL",
    "ERROR_INVALID_IMAGE_URL": "That's not a valid image URL",
    "ERROR_INVALID_COLOR": "That's not a valid color",
    "ERROR_INVALID_JSON": "Invalid JSON!",
    "ERROR_INVALID_ROLE": "Invalid Role",
    "ERROR_INVALID_MAX": "Your max can't be higher than your amount of unique roles",
    "ERROR_INVALID_RESTRICTION_ROLE": "Invalid restriction role(s)",
    "ERROR_MISSING_TITLE_FOR_URL": "When providing a link for the title you need a title",
    "ERROR_MISSING_PERMISSIONS": "You are missing permissions [{0}]",
    "ERROR_NOT_A_GUILD_MEMBER": "That's not a member of this guild",
    "ERROR_REASON_TOO_LONG": "Your reason is too long (max. 200 characters)",
    "ERROR_FUNCTIONBUTTON_NO_RULES": "This server doesn't have any rules",
    "ERROR_NOT_SENT_BY_CLIENT": "That's not a message sent by me",
    "ERROR_NOT_SENT_BY_CLIENT_OLD": "That's not a message sent by me (old)",
    "ERROR_TRANSFER_SAME_URLS": "The old message can't be the new message",
    "ERROR_NOT_SENT_BY_CLIENT_NEW": "That's not a message sent by me (new)",
    "ERROR_TRANSFER_EMBEDS_CONTENTLESS": "The old message can't have no content, select 'copy' true to avoid this",
    "ERROR_COMPONENTS_MOVE_NOT_ENOUGH_BUTTONS": "There aren't enough buttons on this message",
    "ERROR_COMPONENTS_MOVE_NOT_ENOUGH_ROWS": "There aren't enough rows on this message",
    "ERROR_MOVING_DROPDOWNS_UNSUPPORTED": "Moving dropdowns is currently not supported",
    "ERROR_TRANSFER_COMPONENTS_ALREADY_COMPONENTS": "There are already components on the new message",
    "ERROR_BUTTONROLES_INVALID_TYPE": "Invalid type (Valid types: `toggle` `add` `remove`)",
    "ERROR_MESSAGE_EMBED_COUNT": "The total of embeds on the new message can't be larger than 10",
    "ERROR_ACTION_NOT_FOUND": "Unable to find this action",
    "ERROR_MESSAGE_TOO_LONG": "The message is too long (max. 2000 characters)",
    "ERROR_ROLES_NOT_BELOW": "All given roles have to be below me and not managed",
    "ERROR_ROLES_NOT_BELOW1": "All given roles have to be below me",
    "ERROR_ROLES_NOT_BELOW2": "None of the given roles can be managed",
    "ERROR_PURGE_LIMIT": "You can only purge up to 100 messages",
    "ERROR_PURGE_MESSAGES_TOO_OLD": "The messages are older than 14 days and can't be deleted",
    "ERROR_SWITCH_MANAGED_ROLES": "You can't hand out or remove managed roles",
    "ERROR_BUTTONROLE_SWITCH_SAME_ROLE": "You can't remove and add the same role",
    "ERROR_NOT_A_TEXT_CHANNEL": "That's not a text channel",
    "ERROR_WARN_YOURSELF": "You can't warn yourself",
    "ERROR_BAN_YOURSELF": "You can't ban yourself",
    "ERROR_KICK_YOURSELF": "You can't kick yourself",
    "ERROR_MUTE_YOURSELF": "You can't (un)mute yourself",
    "ERROR_MUTE_TOO_LONG": "You can't mute members longer than 28 days",
    "ERROR_UNABLE_TO_MUTE": "I'm unable to (un)mute that member",
    "ERROR_MESSAGE_DELETED": "Don't delete the message!",
    "ERROR_EMOJI_INACCESSIBLE": "At least one emoji is invalid or inaccessable to me",
    "ERROR_COMMAND_OUTSIDE_GUILD": "You can only use commands in guilds",
    "ERROR_EXTERNAL_LINK": "That's not a valid link from this server",
    "ERROR_EXTERNAL_LINK_OLD": "That's not a valid link from this server (old)",
    "ERROR_EXTERNAL_LINK_NEW": "That's not a valid link from this server (new)",
    "ERROR_2_EMOJIS_NEEDED": "When providing custom emojis you need to give at least 2 unicode emojis",
    "ERROR_LEVEL2_NEEDED": "This server needs level 2 for this to work (access to private threads)",
    "ERROR_EMBED_REMOVE_EDIT_ERROR": "Removing all embeds on this message is not supported or your components have invalid emojis",
    "ERROR_CONFIGURATION_ALREADY_SPECIFIED": "This configuration (combination of role + restriction roles) has already been specified. You can't have duplicate ones.",
    "ERROR_EMBED_INVALID_JSON": "Please make sure you pass at least one valid embed",
    "ERROR_EMBED_INVALID_STRUCTURE": "Invalid embed structure!",
    "ERROR_NO_EMBED_IN_POSITION": "There's no embed in position {0}",
    "ERROR_OPEN_THREAD": "You already have a thread opened (<#{0}>)",
    "ERROR_DMS_CLOSED": "\nThe member has their DMs closed",
    "ERROR_CANT_SEND_TO_THIS_CHANNEL": "I'm not able to send a message to that channel",
    "ERROR_CANT_SEND_TO_THAT_CHANNEL": "I'm missing permissions to send messages in the channel the message is in",
    "ERROR_CANT_SEND_TO_THiS_CHANNEL_CHECK": "I'm not able to send a message to that channel so I can't check",
    "ERROR_NOT_A_DEV": "You're not a developer",
    "ERROR_NO_DROPDOWN_IN_ROW": "There's no dropdown in the selected row",
    "ERROR_NOT_A_DROPDOWNROLE_SETUP": "That's not a dropdownrole setup",
    "ERROR_DROPDOWNROLES_ALREADY_SELECTED": "<:SystemMessageInteractionFail:872222564557127680> You already selected options from this DropdownRoles setup.",
    "ERROR_DUPLICATE_ROLES": "You can't have duplicate roles",
    "ERROR_AT_LEAST_2_ROLES": "You need at least 2 unique roles",
    "ERROR_AT_LEAST_X_ROLES": "You need at least {0} unique roles",
    "ERROR_FATAL_MISSING_PERMISSIONS": "I'm missing permissions to perform this action",
    "ERROR_FATAL_MISSING_ACCESS": "I'm missing access",
    "ERROR_UNKNOWN": "Something went wrong",
    "OTHER_BUTTON": "Other Button",
    "ERROR": "Error",
    "UNBAN_SUCCESS": "I unbanned **{0}** (`{1}`) on <@{2}> request",
    "OFFENDER_WARNED": "**You've been warned in __{0}__ for:**\n{1}",
    "OFFENDER_WARNED_REASONLESS": "**You've been warned in __{0}__**",
    "OFFENDER_KICKED": "**You've been kicked from __{0}__ for:**\n{1}",
    "OFFENDER_MUTED": "**You've been muted in __{0}__ for:**\n{1}\nYou will be unmuted <t:{2}:R>",
    "INFO_DESCRIPTION": "SlashBot is a new innovative bot with useful slash commands that replaces ReactionRoles with a simpler UI and user friendly notes.\nGet started by setting up a ButtonRole or a DropdownRole setup by typing `/buttonrole` or `/dropdownroles`!\n\n**Useful Links**\n[Support Server]({0}) **|** [Recommended Invite]({1}) **|** [Bot Page]({2}) **|** [Website]({3}) **|** [Patreon]({4})\n[Contribute to Localization]({5})",
    "HELP_TEXT": "Find detailed help on [our website]({0})\nor in our [support server]({1})",
    "ACTIVITIES_RESPONSE": "[Click to join {0}]({1})",
    "COPYMESSAGE_SUCCESS": "Copied [this message]({0})",
    "COPYMESSAGE_SUCCESS_CHANNEL": "I copied [the message]({0}){1}",
    "BAN_REASON_RESPONSE": "**{0} has been banned for:**\n{1}{2}",
    "PRONOUNS_CLICK_BELOW": "Select your pronouns by clicking below",
    "ASSETS_MISSING_ASSETS": "This user doesn't have any assets",
    "PERMISSIONS_FOR_SERVER": "For this server",
    "MESSAGEINFO_LINKBUTTON": "LinkButton **URL** [click here]({0})",
    "PERMISSIONS_FOR_CHANNEL": "For this channel",
    "MESSAGEINFO_DESCRIPTION": "Information about components on my [message]({0}):\n\n{1}",
    "MESSAGEINFO_TITLE_FORMAT": "Message JSON",
    "DROPDOWNROLES_NO_CHANGES": "No roles have been changed",
    "DROPDOWNROLES_ADDED_ROLES": "Added Roles",
    "DROPDOWNROLES_REMOVED_ROLES": "Removed Roles",
    "DROPDOWNROLES_REMOVED_ALL": "Removed all selectable roles",
    "NO_COMPONENTS": "There are no components on this message",
    "COPYMESSAGE_UNABLE_TO_FETCH": "Unable to fetch targeted message",
    "DROPDOWNROLES_CHANGES_DESCRIPTION": "**You are missing some role(s)**\nYou are missing one or more roles for each role you have selected.\n\n*` Selected role -> Required roles `*",
    "COMMANDHANDLER_PERMISSIONS_NEEDED": "This command requires `{0}` more (global) permission(s): ```diff\n{1}```Add them to my integration role to fix this.",
    "BUTTONROLE_SUCCESS_DESCRIPTION": "**Role(s)** <@&{0}>\n**Notification** {1}\n**Type** {2}\n**Message** [Click here]({3}){4}",
    "BUTTONROLE_SUCCESS_TITLE": "ButtonRole successfully added",
    "BUTTONROLE_REQUIRED_ROLE": "\n**Required Role** <@&{0}>",
    "TRANSFER_EMBEDS_AND_REPLACED": " and replaced the old ones",
    "TRANSFER_EMBEDS_RESPONSE": "{0} all embeds from the [old message]({1}) to the [new message]({2}){3}",
    "TRANSFER_COMPONENTS_RESPONSE": "{0} all components from the [old message]({1}) to the [new message]({2})",
    "SLOWMODE_SET_TO": "set to",
    "IN_CHANNEL": " in <#{0}>",
    "TO_CHANNEL": " to <#{0}>",
    "SLOWMODE_RESPONSE": "Slowmode {0}{1}{2}{3}",
    "SAY_RESPONSE": "Added a say button with the text:\n{0}\nto [this message]({1})",
    "PURGE_RESPONSE": "{0} messages{1} purged",
    "POLL_NEW_POLL": "New Poll by {0}",
    "POLL_CREATED": "Poll{0} created successfully",
    "REMOVE_EMBEDS_IN_POSITION": "Removed the embed on the [message]({0}) in position {1} (attached below)",
    "REMOVE_EMBEDS_ALL": "Removed all embeds from the [message]({0}) (attached below)",
    "FUNCTIONBUTTON_SERVER_RULES": "Server Rules {0}",
    "REMOVE_COMPONENTS_SELECT": "Select which component you want to remove from [this message]({0}) below",
    "REMOVE_COMPONENTS_TITLE": "Components removed",
    "REMOVE_COMPONENTS_DESCRIPTON": "**Removed** {0}",
    "REMOVE_COMPONENTS_ALL": "All components",
    "REMOVE_COMPONENTS_POSITION": "Position {0}",
    "MUTE_ISNT_MUTED": "{0} currently isn't muted",
    "MUTE_UNMUTED_IN": "{0} will be unmuted <t:{1}:R>",
    "LINKBUTTON_TITLE": "LinkButton added",
    "LINKBUTTON_DESCRIPTION": "**Website** [{0}]({1})\n**Message** [click here]({2})",
    "FUNCTIONBUTTON_TITLE": "FunctionButton added",
    "FUNCTIONBUTTON_DESCRIPTION": "**Function** {0}\n**Message** [click here]({1})",
    "EMOJI_TITLE": "EmojiInfo • {0}",
    "EMOJI_DESCRIPTION": "**Animated** {0}\n**Name** {1}\n**ID** {2}\n**File** [click here]({3}){4}",
    "EMOJI_ADDED": "\n**Emoji added**",
    "COMMANDS_OVERVIEW": "Commands Overview",
    "COMMANDS_DESCRIPTION": "**Permissions needed**\n**You** {0}\n**Me** {1}",
    "EMBED_CREATED_JSON": "Embed{0} created with raw JSON",
    "EMBED_CREATED": "Embed{0} created with {1} argument(s)",
    "EMBED_ADDED": "Embed added to [message]({0}) with {1} argument(s)",
    "EMBED_EDITED": "Embed on [message]({0}) edited with {1} argument(s)",
    "EMBED_SHORTEN_TITLE": "Please shorten your title by {0} characters",
    "EMBED_SHORTEN_DESCRIPTION": "Please shorten your description by {0} characters",
    "EMBED_SHORTEN_FOOTER": "Please shorten your footer by {0} characters",
    "EMBED_SHORTEN_STRINGS": "Please shorten any of your strings to be under 6000 characters of title, description and footer in total",
    "EMBED_EDIT_REPLACE_QUESTION": "By providing more than 1 embed all embeds will be replaced with the new one.\nDo you want to replace the old embeds with the new embeds?",
    "EMBED_EDIT_ONLY_ONE_EMBED": "Please provide only one embed",
    "EMBED_EDIT_FIRST_IN_POSITION": "The first embed is in position 1",
    "EMBED_EDIT_NO_EMBED": "There's no embed at that position",
    "EMBED_EDIT_JSON": "Embed on [message]({0}) edited with raw json",
    "DROPDOWNROLES_EDIT_ROLES_INSTRUCTIONS": "Please send a message with the following format:\n```md\n@{0} <role> <emoji> <label>\n<description>\n<restriction role>\n```\n`- ` A label can be any text less than 100 characters\n`- ` An emoji can be any emoji or none\n`- ` Between the role, emoji and label and the description a newline has to exist\n`- ` Restriction role being a role the member needs to select this option",
    "DROPDOWNROLES_ADVANCED_ROLES_INSTRUCTION": "Please send the next messages with the following format:\n```md\n@{0} <role> <emoji> <label>\n<description>\n<restriction roles>\n```\n`- ` A label can be any text less than 100 characters\n`- ` An emoji can be any emoji or `none`\n`- ` Maximum 25 roles\n`- ` Between the role, emoji and label and the description a newline has to exist\n`- ` Restriction roles being a set of roles which the member needs 1 of to get the role (max 4)\n\nSend `done` to finish or `cancel` to cancel",
    "BUTTONROLES_ADVANCED_ROLES_INSTRUCTION": "Please send the next messages with the following format:\n```md\n@{0} <role> <mode> <style> <emoji> <label>\n<required role>```\n`- ` [The style must be a number between 1 and 4](https://discord.com/assets/7bb017ce52cfd6575e21c058feb3883b.png)\n<:empty:708946760277688363>`- ` **{1}**: Primary\n<:empty:708946760277688363>`- ` **{2}**: Secondary\n<:empty:708946760277688363>`- ` **{3}**: Success\n<:empty:708946760277688363>`- ` **{4}**: Destructive\n`- ` The mode must be a one of the following\n<:empty:708946760277688363>`- ` **toggle**: Allows adding and removing\n<:empty:708946760277688363>`- ` **add**: Allows only adding\n<:empty:708946760277688363>`- ` **remove**: Allows only removing\n`- ` A label **or** emoji must be provided\n`- ` A label can be any text less than 100 characters or none\n`- ` An emoji can be any emoji, `default` or `none`\n`- ` Maximum 25 roles\n`- ` There must be a newline before the required role\n`- ` The role required to use the button\nSend `done` to finish or `cancel` to cancel",
    "DROPDOWNROLES_EDIT_ROLES_TITLE": "Add Option",
    "DROPDOWNROLES_EDIT_ROLES_NO_MESSAGE": "No message given",
    "DROPDOWNROLES_EDIT_ROLES_ADDED": "Added role <@&{0}> to the DropdownRoles setup in row {1} on [this message]({2})",
    "DROPDOWNROLES_EDIT_ROLES_REMOVED": "Removed role <@&{0}> from the DropdownRoles setup in row {1} on [this message]({2})",
    "DROPDOWNROLES_SELECT_UP_TO": "Select up to {0} roles",
    "DROPDOWNROLES_SELECT_ONE_OF": "Select one of {0} roles",
    "DROPDOWNROLES_EDIT_NO_VALUE_SELECTED": "You didn't select a value",
    "DROPDOWNROLES_EDIT_SELECT_OPTION": "Select the option you want to remove",
    "DROPDOWNROLES_EDIT_INVALID_DROPDOWN": "You can't remove any more options from this dropdown",
    "DROPDOWNROLES_EDIT_APPEARANCE_MAX_ROLES": "Please set your max_roles to something equal or lower than the options count",
    "DROPDOWNROLES_EDIT_APPEARANCE_NOTIFICATION_ENABLED": "You already have notifications enabled",
    "DROPDOWNROLES_EDIT_APPEARANCE_NOTIFICATION_DISABLED": "You already have notifications disabled",
    "DROPDOWNROLES_EDIT_APPEARANCE_RESELECTABLE_ENABLED": "This DropdownRoles setup is already reselectable",
    "DROPDOWNROLES_EDIT_APPEARANCE_RESELECTABLE_DISABLED": "This DropdownRoles setup is already locked to one selection only",
    "DROPDOWNROLES_EDIT_APPEARANCE_NOTHING_EDITED": "You need to edit at least one property",
    "DROPDOWNROLES_EDIT_APPEARANCE_REPLY": "I edited the options {0} on [this message]({1})",
    "DROPDOWNROLES_SET_UP": "DropdownRoles set up",
    "BUTTONROLE_SETUP": "ButtonRole setup",
    "DROPDOWNROLES_ADDED": "DropdownRoles setup added",
    "DROPDOWNROLES_CANCELLED": "DropdownRoles setup cancelled",
    "DROPDOWNROLES_CREATE_DESCRIPTION": "**Channel** <#{0}>\n**Roles** {1}\n**Max Roles** {2}",
    "DROPDOWNROLES_ADD_DESCRIPTION": "**Role(s)** {0}\n**Max Roles** {1}\n**Notify** {2}\n**Message** [Click here]({3})",
    "DROPDOWNROLES_BULK_SETUP": "DropdownRoles bulk setup",
    "DROPDOWNROLES_ADVANCED_ADD_DESCRIPTION": "**Message** [Click here]({0})\n**Roles** {1}\n**Max Values** {2}",
    "DROPDOWNROLES_EXPIRED": "The set up timed out after 5 minutes",
    "COMPONENTS_SETSTATE_REPLY": "All components on [this message]({0}) have been {1}",
    "COMPONENTS_MOVE_BUTTONS_TITLE": "Move Button",
    "COMPONENTS_MOVE_ROW_TITLE": "Move Row",
    "COMPONENTS_MOVE_DESCRIPTION1": "Click the button below representing the button (from [this message]({0})) you want to move",
    "COMPONENTS_MOVE_DESCRIPTION2": "Click the button below representing the position (on [this message]({0})) you want to move the button to.\n\n**Button to move** {1}",
    "COMPONENTS_MOVE_DESCRIPTION3": "Moving on [this message]({0}) complete.\n\n**Button to move** {1}\n**Position to move to** {2}",
    "COMPONENTS_MOVE_ROW_DESCRIPTION1": "Click the button below representing the row (from [this message]({0})) you want to move",
    "COMPONENTS_MOVE_ROW_DESCRIPTION2": "Click the button below representing the position (on [this message]({0})) you want to move the row to.\n\n**Row to move** {1}",
    "COMPONENTS_MOVE_ROW_DESCRIPTION3": "Moving on [this message]({0}) complete.\n\n**Row to move** {1}\n**Position to move to** {2}",
    "COMPONENTS_CHECK_SUCCESS": "✅ All roles on this message are still fine",
    "COMPONENTS_CHECK_INVALID": "❌ `Faulty components: {0}. Do you want me to remove them?`",
    "COMPONENTS_CHECK_DISMISS": "You chose not to remove the faulty components.\nKeep in mind that you will not be able to edit this message in any way as long as it has faulty components in it.",
    "COMPONENTS_CHECK_REMOVE_SUCCESS": "All {0} faulty components [on this message]({1}) have been removed successfully",
    "BUTTONROLES_SET_UP": "ButtonRoles set up",
    "BUTTONROLES_SETUP_CANCELLED": "ButtonRoles setup cancelled",
    "BUTTONROLES_SWITCH_DESCRIPTION_CREATE": "**Channel** <#{0}>\n**Notification** {1}\n**Role to remove** <@&{2}>\n**Role to give** <@&{3}>\n**Type** Switch{4}",
    "BUTTONROLES_SWITCH_DESCRIPTION_ADD": "**Message** [click here]({0})\n**Notification** {1}\n**Role to remove** <@&{2}>\n**Role to give** <@&{3}>\n**Type** Switch{4}",
    "BUTTONROLES_CREATE_DESCRIPTION": "**Channel** <#{0}>\n**Notification** {1}\n**Role(s)** {2}\n**Type** {3}{4}",
    "BUTTONROLES_ADVANCED": "**Channel** <#{0}>\n**Roles** {1}"
}
for key in template_data.keys():
      if key not in en_data:
        print(f"\"{key}\": \"\",")

print("\n\n")
data={
"ERROR_BUTTONROLE_ALREADY_HAVE": "",
"ERROR_BUTTONROLE_DONT_HAVE": "",
"ERROR_BUTTONROLE_EVERYONE_SET_UP": "",
"ERROR_COMPONENTS_MOVE_NOT_ENOUGH_ROWS": "",
"ERROR_ROLES_NOT_BELOW1": "",
"ERROR_ROLES_NOT_BELOW2": "",
"ERROR_MUTE_TOO_LONG": "",
"ERROR_NOT_A_DEV": "",
"ERROR_DROPDOWNROLES_ALREADY_SELECTED": "",
"ERROR_FATAL_MISSING_PERMISSIONS": "",
"ERROR_FATAL_MISSING_ACCESS": "",
"DROPDOWNROLES_EDIT_APPEARANCE_RESELECTABLE_ENABLED": "", 
"DROPDOWNROLES_EDIT_APPEARANCE_RESELECTABLE_DISABLED": "",
"COMPONENTS_MOVE_BUTTONS_TITLE": "",
"COMPONENTS_MOVE_ROW_TITLE": "",
"COMPONENTS_MOVE_ROW_DESCRIPTION1": "",
"COMPONENTS_MOVE_ROW_DESCRIPTION2": "",
"COMPONENTS_MOVE_ROW_DESCRIPTION3": ""
}
for key in template_data.keys():
      if key in data:
        print(f"\"{key}\": \"{template_data[key]}\",")

