local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
	return
end

require 'lsp.lsp_installer'
require 'lsp.settings.sumneko_lua'
-- require 'lsp.settings.pyright'
require('lsp.handlers').setup()
