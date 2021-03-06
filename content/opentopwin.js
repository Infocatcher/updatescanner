/* ***** BEGIN LICENSE BLOCK *****
 * Version: MPL 1.1/GPL 2.0/LGPL 2.1
 *
 * The contents of this file are subject to the Mozilla Public License Version
 * 1.1 (the "License"); you may not use this file except in compliance with
 * the License. You may obtain a copy of the License at
 * http://www.mozilla.org/MPL/
 *
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 *
 * The Original Code is mozilla.org code.
 *
 * The Initial Developer of the Original Code is
 * Netscape Communications Corporation.
 * Portions created by the Initial Developer are Copyright (C) 1998
 * the Initial Developer. All Rights Reserved.
 *
 * Contributor(s):
 *   Alec Flett <alecf@netscape.com>
 *   Pete Burgers <updatescanner@gmail.com>
 *
 * Alternatively, the contents of this file may be used under the terms of
 * either of the GNU General Public License Version 2 or later (the "GPL"),
 * or the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *
 * ***** END LICENSE BLOCK ***** */
 
 /* These functions are from the Thunderbird source (utilityOverlay.js) */

if (typeof(USc_topWin_exists) != 'boolean') {
var USc_topWin_exists = true;
var USc_topWin = {    
 
get : function()
{
    var windowManager = Components.classes['@mozilla.org/appshell/window-mediator;1'].getService();
    var windowManagerInterface = windowManager.QueryInterface( Components.interfaces.nsIWindowMediator);
    var topWindowOfType = windowManagerInterface.getMostRecentWindow( "navigator:browser" );

    if (topWindowOfType) {
        return topWindowOfType;
    }
    return null;
},

open : function(url)
{
    if ((url == null) || (url == "")) return null;

    // xlate the URL if necessary
    if (url.indexOf("urn:") == 0)
    {
        url = xlateURL(url);        // does RDF urn expansion
    }

    // avoid loading "", since this loads a directory listing
    if (url == "") {
        url = "about:blank";
    }

    var topWindowOfType = USc_topWin.get();
    if ( topWindowOfType )
    {
        topWindowOfType.focus();
        topWindowOfType.loadURI(url);
        return topWindowOfType;
    }
    return window.openDialog( getBrowserURL(), "_blank", "chrome,all,dialog=no", url );
}
}
}