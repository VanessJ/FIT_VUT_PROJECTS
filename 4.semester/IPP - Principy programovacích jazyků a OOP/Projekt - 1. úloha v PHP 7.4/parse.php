<?php

# Name: parse.php
# Author: Vanessa Jóriová xjorio00
# Login: xjorio00
# Date: 17.3.2021

ini_set('display_errors', 'stderr');
define("PARAM_ERR", 10); //chybajuci parameter, zakazana kombinacia
define("INPUT_FILE_ERROR", 11); //vstupne subory, neexistencia atd.
define("OUTPUT_FILE_ERROR", 12); //vystupne subory
//error codes
define("OK", 0);
define("ERR_HEADER", 21);
define("ERR_OPCODE", 22);
define("ERR_LEX_SYN", 23);

//regex
define("labelRegex", "/^[a-zA-Z_\-$&%*!?][0-9a-zA-Z_\-$&%*!?]*$/");
define("varRegex", "/^(GF|LF|TF)@[a-zA-Z_\-$&%*!?][0-9a-zA-Z_\-$&%*!?]*$/");
define("boolRegex", "/^(true|false)$/");
define("nilRegex", "/^nil$/");
define("intRegex", "/^[+-]?\d+$/");
define("stringRegex",  "/^(?!.*(\\\\\d\d\D|\\\\\d\d$|\\\\\d\D|\\\\\d$|\\\\\D|\\\\$|\s)).*$/m");
define("typeRegex", "/^(string|int|bool)$/");


$loc = 0;
$comments = 0;
$jumps = 0;
$labels = 0;
$fwjumps = 0;
$backjumps = 0;
$badjumps = 0;
$labelArray = [];
$jumpArray = [];



function printStats()
{
    
    global $argv;
    global $loc;
    global $comments;
    global $jumps;
    global $labels;
    global $fwjumps;
    global $backjumps;
    global $badjumps;


    $handle = NULL;


    for ($i = 1; $i < (count($argv)); $i++) {
        $parts = explode("=", $argv[$i], 2);
        switch ($parts[0]) {
            case "--stats":
                if (!file_exists($parts[1])) {
                    errorExit(INPUT_FILE_ERROR, "File doesn't exist");
                }
                $handle = fopen($parts[1], "r+");
                if (!$handle) {
                    errorExit(INPUT_FILE_ERROR, "Couldn't open file");
                }
                break;

            case "--loc":
                fwrite($handle, $loc . "\n");
                break;

            case "--comments":
                fwrite($handle, $comments . "\n");
                break;

            case "--labels":
                fwrite($handle, $labels . "\n");
                break;

            case "--jumps":
                fwrite($handle, $jumps . "\n");
                break;

            case "--fwjumps":
                fwrite($handle, $fwjumps . "\n");
                break;

            case "--backjumps":
                fwrite($handle, $backjumps . "\n");
                break;

            case "--badjumps":
                fwrite($handle, $badjumps . "\n");
                break;
            default:
                errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
        }
    }
}


function errorExit($retval, $msg)
{
    error_log("\e[31m$msg");
    exit($retval);
}

function checkArgs()
{
    global $argc;
    global $argv;
    $helpMessege = "Script načíta zo štandardného vstupu medzikód IPPcode21, spraví základné lexikálne a syntaktické kontroly a vypíše programovú reprezentáciu v XML.\nPre viac info o prepínačoch viz. https://wis.fit.vutbr.cz/FIT/st/cfs.php/course/IPP-IT/projects/2020-2021/Zadani/ipp21spec.pdf\n";
    $statfound = false;
    $handle = NULL;
    $files_aray = [];


    for ($i = 1; $i < (count($argv)); $i++) {
        $parts = explode("=", $argv[$i], 2);
        switch ($parts[0]) {
            case "--help":
                if ($argc > 2) {
                    errorExit(PARAM_ERR, "Viac argumentov pri --help, chyba 10");
                }
                echo ($helpMessege);
                exit(OK);
                break;

            case "--stats":
                if (count($parts) != 2) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                } else {
                    $statfound = true;

                    if ($handle != NULL) {
                        fclose($handle);
                    }

                    $handle = fopen($parts[1], "w");
                    if (!$handle) {
                        errorExit(INPUT_FILE_ERROR, "Couldn't open file");
                    }
                    if (in_array($parts[1], $files_aray)) {
                        errorExit(OUTPUT_FILE_ERROR, "Cannot write statistics twice into same file");
                    }
                    array_push($files_aray, $parts[1]);
                }
                break;

            case "--loc":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            case "--comments":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            case "--labels":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            case "--jumps":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            case "--fwjumps":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            case "--backjumps":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            case "--badjumps":
                if ((count($parts) != 1) || ($statfound == false)) {
                    errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
                }
                break;

            default:
                errorExit(PARAM_ERR, "Wrong parameters. For more info try --help");
        }
    }
}

function checkSymbol($symbol)
{
    if ($checktype = (checkType($symbol) == OK) || (($checkvar = checkVar($symbol) == OK))) {
        return OK;
    } else {
        return ERR_LEX_SYN;
    }
}

function checkRead($type)
{
    if (preg_match(typeRegex, $type)) {
        return OK;
    } else {
        return ERR_LEX_SYN;
    }
}


function checkType($symbol)
{
    $type = preg_split('/@/', $symbol, 2);
    switch ($type[0]) {

        case "nil":
            if (preg_match(nilRegex, $type[1])) {
                return OK;
            }
            //if (sizeof($type) != 2)
            break;
        case "int":
            if (preg_match(intRegex, $type[1])) {
                return OK;
            }
            break;
        case "bool":
            if (preg_match(boolRegex, $type[1])) {
                return OK;
            }
            break;
        case "string":
            if (preg_match(stringRegex, $type[1])) {
                return OK;
            }
            break;

        default:
            return ERR_LEX_SYN;
    }

    return ERR_LEX_SYN;
}


//checking for .IPPcode21
function checkHeader()
{

    global $comments;
    while (!feof(STDIN)) {

        $line = (fgets(STDIN));
        $line = strtolower(preg_replace("/#.*$/", "", $line, -1, $found));    // Remove commentary
        if ($found) {
            $comments++;
        }
        $line = trim($line);

        if ($line == '') {
            continue;
        }

        if ($line != ".ippcode21") {
            return false;
        } else {
            return true;
        }
    }
    return false;
}


function checkLabel($label)
{
    if (preg_match(labelRegex, $label)) {
        return OK;
    } else {
        return ERR_LEX_SYN;
    }
}

function checkVar($var)
{
    if (preg_match(varRegex, $var)) {
        return OK;
    } else {
        return ERR_LEX_SYN;
    }
}

function checkCodeGenerateTree($code)
{
    global $counter;
    global $dom_doc;
    global $xml_tree;
    global $loc; //loc counter
    global $labels;
    global $jumps;
    global $labelArray;
    global $jumpArray;
    global $backjumps;


    $counter++;
    $xml_instruction = $dom_doc->createElement("instruction");
    $xml_instruction->setAttribute("order", $counter);
    $xml_instruction->setAttribute("opcode", strtoupper($code[0]));
    $code[0] = strtoupper($code[0]);
    switch ($code[0]) { //instruction

            //opcode
        case "CREATEFRAME":
        case "POPFRAME":
        case "PUSHFRAME":
        case "RETURN":
        case "BREAK":

            //extra opcode 
            if (sizeof($code) != 1) {
                return ERR_LEX_SYN;
            }

            if ($code[0] == "RETURN") {
                $jumps++;
            }

            $loc++;
            break;


            //opcode <label>
        case "LABEL":
        case "JUMP":
        case "CALL":

            if (sizeof($code) != 2) {
                return ERR_LEX_SYN;
            }

            if (checkLabel($code[1]) != OK) {
                return ERR_LEX_SYN;
            }

            $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
            $xml_arg1->setAttribute("type", "label");
            $xml_instruction->appendChild($xml_arg1);

            if ($code[0] == "LABEL") {
                array_push($labelArray, $code[1]);
                $labels++;
            } else if ($code[0] == "JUMP" || $code[0] == "CALL") {
                $jumps++;
                if (in_array($code[1], $labelArray)) { //was label already read?
                    $backjumps++;
                } else {
                    array_push($jumpArray, $code[1]); //add label for later check
                }
            }
            $loc++;
            break;

            //opcode <var>
        case "DEFVAR":
        case "POPS":
            if (sizeof($code) != 2) {
                return ERR_LEX_SYN;
            }

            if (checkVar($code[1]) != OK) {
                return ERR_LEX_SYN;
            }

            $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
            $xml_arg1->setAttribute("type", "var");
            $xml_instruction->appendChild($xml_arg1);

            $loc++;
            break;

            //opcode <symb>
        case "PUSHS":
        case "WRITE":
        case "EXIT":
        case "DPRINT":
            if (sizeof($code) != 2) {
                return ERR_LEX_SYN;
            }

            if (checkSymbol($code[1]) != OK) {
                return ERR_LEX_SYN;
            }

            if (checkVar($code[1]) == OK) { //variable, not constant
                $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
                $xml_arg1->setAttribute("type", "var");
            } else {
                $parts = preg_split('/@/', $code[1], 2);
                $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($parts[1]));
                $xml_arg1->setAttribute("type", $parts[0]);
            }

            $xml_instruction->appendChild($xml_arg1);

            $loc++;
            break;

            //opcode <var> <symb>
        case "MOVE":
        case "STRLEN":
        case "TYPE":
        case "NOT":
            if (sizeof($code) != 3) {
                return ERR_LEX_SYN;
            }

            if (checkVar($code[1]) != OK) {
                return ERR_LEX_SYN;
            }

            if (checkSymbol($code[2]) != OK) {
                return ERR_LEX_SYN;
            }

            // <var>
            $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
            $xml_arg1->setAttribute("type", "var");

            // <symb>
            if (checkVar($code[2]) == OK) { //variable, not constant
                $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($code[2]));
                $xml_arg2->setAttribute("type", "var");
            } else {
                $parts = preg_split('/@/', $code[2], 2);
                $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($parts[1]));
                $xml_arg2->setAttribute("type", $parts[0]);
            }

            $xml_instruction->appendChild($xml_arg1);
            $xml_instruction->appendChild($xml_arg2);

            $loc++;
            break;

            //opcode <var> <type>
        case "READ":
            if (sizeof($code) != 3) {
                return ERR_LEX_SYN;
            }

            if (checkVar($code[1]) != OK) {
                return ERR_LEX_SYN;
            }
            if (checkRead($code[2]) != OK) {
                return ERR_LEX_SYN;
            }

            //<var> 
            $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
            $xml_arg1->setAttribute("type", "var");

            //<type>
            $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($code[2]));
            $xml_arg2->setAttribute("type", "type");

            $xml_instruction->appendChild($xml_arg1);
            $xml_instruction->appendChild($xml_arg2);

            $loc++;
            break;

            //opcode <var> <symb> <symb>
        case "ADD":
        case "SUB":
        case "MUL":
        case "IDIV":
        case "LT":
        case "GT":
        case "EQ":
        case "AND":
        case "OR":
        case "STRI2INT":
        case "CONCAT":
        case "GETCHAR":
        case "SETCHAR":

            if (sizeof($code) != 4) {
                return ERR_LEX_SYN;
            }

            if (checkVar($code[1]) != OK) {
                return ERR_LEX_SYN;
            }

            if (checkSymbol($code[2]) != OK) {
                return ERR_LEX_SYN;
            }

            if (checkSymbol($code[3]) != OK) {
                return ERR_LEX_SYN;
            }

            //<var>
            $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
            $xml_arg1->setAttribute("type", "var");

            // <symb1>
            if (checkVar($code[2]) == OK) { //variable, not constant
                $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($code[2]));
                $xml_arg2->setAttribute("type", "var");
            } else {
                $parts = preg_split('/@/', $code[2], 2);
                $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($parts[1]));
                $xml_arg2->setAttribute("type", $parts[0]);
            }

            // <symb2>
            if (checkVar($code[3]) == OK) { //variable, not constant
                $xml_arg3 = $dom_doc->createElement("arg3", htmlspecialchars($code[3]));
                $xml_arg3->setAttribute("type", "var");
            } else {
                $parts = preg_split('/@/', $code[3], 2);
                $xml_arg3 = $dom_doc->createElement("arg3", htmlspecialchars($parts[1]));
                $xml_arg3->setAttribute("type", $parts[0]);
            }

            $xml_instruction->appendChild($xml_arg1);
            $xml_instruction->appendChild($xml_arg2);
            $xml_instruction->appendChild($xml_arg3);

            $loc++;
            break;

            //opcode <label> <symb> <symb>
        case "JUMPIFEQ":
        case "JUMPIFNEQ":

            if (sizeof($code) != 4) {
                return ERR_LEX_SYN;
            }

            if (checkLabel($code[1]) != OK) {
                return ERR_LEX_SYN;
            }

            if (checkSymbol($code[2]) != OK) {
                return ERR_LEX_SYN;
            }

            if (checkSymbol($code[3]) != OK) {
                return ERR_LEX_SYN;
            }

            if (in_array($code[1], $labelArray)) { //was label already read?
                $backjumps++;
            } else {
                array_push($jumpArray, $code[1]); //add label for later check
            }

            //<label>
            $xml_arg1 = $dom_doc->createElement("arg1", htmlspecialchars($code[1]));
            $xml_arg1->setAttribute("type", "label");
            $xml_instruction->appendChild($xml_arg1);

            // <symb1>
            if (checkVar($code[2]) == OK) { //variable, not constant
                $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($code[2]));
                $xml_arg2->setAttribute("type", "var");
            } else {
                $parts = preg_split('/@/', $code[2], 2);
                $xml_arg2 = $dom_doc->createElement("arg2", htmlspecialchars($parts[1]));
                $xml_arg2->setAttribute("type", $parts[0]);
            }

            // <symb2>
            if (checkVar($code[3]) == OK) { //variable, not constant
                $xml_arg3 = $dom_doc->createElement("arg3", htmlspecialchars($code[3]));
                $xml_arg3->setAttribute("type", "var");
            } else {
                $parts = preg_split('/@/', $code[3], 2);
                $xml_arg3 = $dom_doc->createElement("arg3", htmlspecialchars($parts[1]));
                $xml_arg3->setAttribute("type", $parts[0]);
            }

            $xml_instruction->appendChild($xml_arg1);
            $xml_instruction->appendChild($xml_arg2);
            $xml_instruction->appendChild($xml_arg3);

            $loc++;
            $jumps++;
            break;

        default:
            return ERR_OPCODE;
    }

    $xml_tree->appendChild($xml_instruction);
}


//main


checkArgs();
//create DOM document
$dom_doc = new DOMDocument('1.0', 'utf-8');
$dom_doc->formatOutput = true;

//XML config
$xml_tree = $dom_doc->createElement("program");
$xml_tree->setAttribute("language", "IPPcode21");
$xml_tree = $dom_doc->appendChild($xml_tree);

if (checkHeader() == false) {
    errorExit(ERR_HEADER, "Missing or wrong header");
}
while (!feof(STDIN)) {

    $line = (fgets(STDIN));
    $line = preg_replace("/#.*$/", "", $line, -1, $found);    // Remove commentary
    if ($found) {
        $comments++;
    }

    $line = trim($line);

    if ($line == '') {
        continue;
    }

    $line = preg_replace('/\s+/', " ", $line);
    $word_arr = explode(" ", $line);
    $result = checkCodeGenerateTree($word_arr);
    if ($result == ERR_OPCODE) {
        errorExit(ERR_OPCODE, "Wrong operation code");
    } else if ($result == ERR_LEX_SYN) {
        errorExit(ERR_LEX_SYN, "Wrong syntax");
    }
}

foreach ($jumpArray as &$label) {
    if (in_array($label, $labelArray)) { //was label read?
        $fwjumps++;
    } else {
        $badjumps++;
    }
}

echo $dom_doc->saveXML();
printStats();
