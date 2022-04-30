local map = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true}

vim.g.maplocalleader = ","
vim.g.mapleader = " "
map('i', 'jj', '<Esc>', opts) 
map("n", "<S-l>", ":bnext<CR>", opts)
map("n", "<S-h>", ":bprevious<CR>", opts)
map('n', '<leader>nt', ':NvimTreeToggle<CR>', opts)
map('n', '<leader>nf', ':NvimTreeFocus<CR>', opts)
map('n', '<leader>nff', ':NvimTreeFindFile<CR>', opts)
map('n', '<leader>ff', ':Telescope find_files<CR>', opts)
map('n', '<leader>fg', ':Telescope live_grep<CR>', opts)
map('n', '<leader>fh', ':Telescope help_tags<CR>', opts)

map('n', '<leader>zfn', ':Telekasten find_notes<CR>', opts)
map('n', '<leader>zil', ':Telekasten insert_link<CR>', opts)
map('n', '<leader>zd', ':Telekasten find_daily_notes<CR>', opts)
map('n', '<leader>zsn', ':Telekasten search_notes<CR>', opts)
map('n', '<leader>zfl', ':Telekasten follow_link<CR>', opts)
map('n', '<leader>z', ':Telekasten panel<CR>', opts)
