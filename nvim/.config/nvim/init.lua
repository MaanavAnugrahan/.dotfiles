require 'settings'
require 'plugins'
require 'plugins.nvim-tree'
require 'plugins.bufferline'
require 'plugins.telekasten'
require 'plugins.lualine'
require 'plugins.vimtex'
require 'plugins.vim-markdown'
require 'colors.gruvbox'
require 'mappings'
require 'lsp'
require 'lsp.cmp'
require("transparent").setup({
  enable = true, -- boolean: enable transparent
  extra_groups = { -- table/string: additional groups that should be cleared
    -- In particular, when you set it to 'all', that means all available groups

    -- example of akinsho/nvim-bufferline.lua
    "BufferLineTabClose",
    "BufferlineBufferSelected",
    "BufferLineFill",
    "BufferLineBackground",
    "BufferLineSeparator",
    "BufferLineIndicatorSelected",
  },
  exclude = {}, -- table: groups you don't want to clear
})
require('gitsigns').setup()

