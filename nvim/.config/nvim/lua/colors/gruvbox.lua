local set = vim.opt

vim.opt.termguicolors = true
vim.o.background = "dark"
-- or "light" for light mode.
vim.g.gruvbox_material_diagnostic_virtual_text = "1"
vim.g.gruvbox_material_diagnostic_text_highlight = "1"
vim.g.gruvbox_material_diagnostic_line_highlight = "1"
vim.g.gruvbox_material_transparent_background = "1"
vim.cmd([[colorscheme gruvbox-material]])
